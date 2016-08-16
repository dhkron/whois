from .. import querier

import unittest
import time
import traceback


class GenericParserTestCase(unittest.TestCase):
    def test_parse(self):

        failed = 0
        passed = 0

        for domain in (
            'aboutcookies.org',
            'allaboutcookies.org',
            'ap.org',
            'apache.org',
            'archive.org',
            'bbb.org',
            'creativecommons.org',
            'debian.org',
            'doi.org',
            'drupal.org',
            'gnu.org',
            'icann.org',
            'ieee.org',
            'ietf.org',
            'iso.org',
            'joomla.org',
            'mediawiki.org',
            'moodle.org',
            'mozilla-europe.org',
            'mozilla.org',
            'networkadvertising.org',
            'nginx.org',
            'npr.org',
            'oecd.org',
            'olympic.org',
            'opensource.org',
            'openstreetmap.org',
            'oxfordjournals.org',
            'pbs.org',
            'pewinternet.org',
            'python.org',
            'redcross.org',
            'telnic.org',
            'un.org',
            'unesco.org',
            'unicef.org',
            'w3.org',
            'wikimedia.org',
            'wikipedia.org',
            'wordpress.org',
            'worldbank.org',
        ):
            try:
                whois_querier = querier.Querier()
                parsed = whois_querier.query(domain)
            except Exception as exception:
                print(domain)
                print(''.join(traceback.format_tb(exception.__traceback__)))

            if parsed['creation_date']:
                # print(str(parsed).encode('ascii', 'ignore'))
                passed = passed + 1
            else:
                print(str(parsed).encode('ascii', 'ignore'))
                print(domain)
                failed = failed + 1

            time.sleep(1)

        print("Tests Passed: " + str(passed) + " Tests Failed: " + str(failed))
