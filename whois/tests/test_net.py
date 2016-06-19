from .. import resolver

import unittest
import time
import traceback


class GenericParserTestCase(unittest.TestCase):
    def test_parse(self):
        for domain in (
            'accesstrade.net',
            'authorize.net',
            'behance.net',
            'bola.net',
            'cpanel.net',
            'daum.net',
            'discuz.net',
            'doubleclick.net',
            'fbcdn.net',
            'isimtescil.net',
            'ovh.net',
            'php.net',
            'rs6.net',
            'secureserver.net',
            'slideshare.net',
            'themeforest.net',
            'uk2.net',
            'wordpress-fr.net',
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
