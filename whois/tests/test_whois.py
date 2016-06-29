import concurrent.futures
import tldextract
import traceback
import csv
import bs4
import urllib.request
import subprocess
import shlex

from .. import querier
from .. import resolvers


def get_domains():
    with open('/home/uri/Downloads/domains_prod.txt') as f:
        content = f.readlines()

    for domain in content:
        yield domain

    # with open('/home/uri/Downloads/top-1m.csv') as csvfile:
    #     spamreader = csv.reader(csvfile, delimiter=',')
    #     for row in spamreader:
    #         yield row[1]


def check_domain(domain):
    try:
        tld = tldextract.extract(domain)
        q = querier.Querier()
        try:
            result = q.query(domain.rstrip())
        except querier.DomainIsInvalid:
            print("DomainIsInvalid " + domain.rstrip())
            return

        except querier.WhoIsServerDoesNotExist:
            print("WhoIsServerDoesNotExist " + domain.rstrip())
            return

        except querier.DomainDoesNotExist:
            print("DomainDoesNotExist. " + domain.rstrip())
            return

        except querier.CannotParse:
            print('Bad Domain. No creation_date and no updated_date ' + domain.rstrip())
            return

        except querier.BlockedWhoisRequest:
            print('BlockedWhoisRequest: ' + domain.rstrip())
            return
        except resolvers.program.WhoisTimeout:
            print('WhoisTimeout: ' + domain.rstrip())
            return
        if not result['raw_whois']:
            print("Bad Domain. A raw key was not present. " + domain.rstrip())

        try:
            print("Good Domain. " + domain.rstrip() + " " + result['parsed']['creation_date'].strftime("%d/%m/%y"))
        except Exception as ex:
            if result['parsed']['updated_date']:
                print("Good Domain With Updated Date Only. " + domain.rstrip() + " " + result['parsed']['updated_date'].strftime("%d/%m/%y"))
            else:
                print("Bad Domain. Not time given. " + domain.rstrip())
    except Exception as ex:
        traceback.print_exc()
        if "has no whois server" in str(ex):
            print("Skipped domain. " + tld.suffix)
        else:
            print("Bad Domain. Who Is did not succeed. " + tld.suffix)


def test_who_is():
    # checkedTLDs = []
    # domains_to_check = []
    # for domain in get_domains():
    #     tld = tldextract.extract(domain)
    #     if tld.suffix not in checkedTLDs:
    #         checkedTLDs.append(tld.suffix)
    #         domains_to_check.append(domain)

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        # random.shuffle(domains_to_check)
        for domain in get_domains():
            executor.submit(check_domain, domain)


class WhoIsServerListHandler(object):
    def __init__(self, url):
        self.url = url
        self.page = urllib.request.urlopen(url).read()
        self.mapTLDToDomainServer()

    def parseTLD(self, tld):
        TLDInfo = dict()

        if 'name' in tld.attrs:
            TLDInfo['name'] = tld.attrs['name']

        TLDInfo['source'] = tld.findChildren('source')[0].string
        TLDInfo['created'] = tld.findChildren('created')[0].string
        TLDInfo['changed'] = tld.findChildren('changed')[0].string
        TLDInfo['state'] = tld.findChildren('state')[0].string

        return TLDInfo

    def mapTLDToDomainServer(self):
        soup = bs4.BeautifulSoup(self.page, "lxml")
        tlds = soup.findAll('domain')
        for tld in tlds:
            TLDInfo = self.parseTLD(tld)
            print(TLDInfo)


def show_raw_whois():
    no_creation_date = []
    not_exists = []
    to_fix = []
    with open('/home/uri/Desktop/Bad4.txt') as f:
        content = f.readlines()

    for domain in content:
        try:
            print("\n\n\n\nRunning " + "whois " + domain + "\n\n\n\n")
            completed_process = subprocess.run(
                        args=shlex.split("whois " + domain.rstrip(), posix=True),
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        timeout=10,
                        )
            sout = completed_process.stdout
            print(sout.decode())
            ans = input("To which list  " + domain.rstrip() + " belong?")
            if ans == 'd':
                no_creation_date.append(domain.rstrip())
                continue
            if ans == 'e':
                not_exists.append(domain.rstrip())
                continue
            if ans == 'save':
                # no_creation_date_file = open('/home/uri/Desktop/no_creation_date.txt', "w")
                # not_exists_file = open('/home/uri/Desktop/not_exists.txt', "w")
                # to_fix_file = open('/home/uri/Desktop/to_fix.txt', "w")
                #
                # no_creation_date_file.write("\n".join(no_creation_date))
                # not_exists_file.write("\n".join(not_exists))
                # to_fix_file.write("\n".join(to_fix))
                print("\n\n\nNo creation date: \n\n\n" + "\n".join(no_creation_date))
                print("\n\n\nto_fix: \n\n\n" + "\n".join(to_fix))
                print("\n\n\nnot_exists: \n\n\n" + "\n".join(not_exists))
                continue
            else:
                to_fix.append(ans + " | " + domain.rstrip())
                continue
        except Exception as ex:
            not_exists.append(domain.rstrip())


if "__main__" == __name__:
    # ok = WhoIsServerListHandler('https://raw.githubusercontent.com/whois-server-list/whois-server-list/master/whois-server-list.xml')
    # ok.mapTLDToDomainServer()
    test_who_is()
    # show_raw_whois()
