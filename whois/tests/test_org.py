from .. import resolver

import unittest
import time
import traceback


class GenericParserTestCase(unittest.TestCase):
    def test_parse(self):
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
                whois_resolver = resolver.Resolver()
                parsed = whois_resolver.query(domain)
                parsed = parsed['parsed']
            except Exception as exc:
                print(domain)
                print(''.join(traceback.format_tb(exc.__traceback__)))

            if parsed['creation_date']:
                # print(str(parsed).encode('ascii', 'ignore'))
                pass
            else:
                print(str(parsed).encode('ascii', 'ignore'))
                print(domain)

            time.sleep(1)
