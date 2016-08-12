from .. import querier

import unittest
import time
import traceback


class GenericParserTestCase(unittest.TestCase):
    def test_parse(self):

        failed = 0
        passed = 0

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
                whois_querier = querier.Querier()
                parsed = whois_querier.query(domain)
            except Exception as exc:
                print(domain)
                print(''.join(traceback.format_tb(exc.__traceback__)))

            if parsed['creation_date']:
                # print(str(parsed).encode('ascii', 'ignore'))
                passed = passed + 1
            else:
                print(str(parsed).encode('ascii', 'ignore'))
                print(domain)
                failed = failed + 1

            time.sleep(1)

            print("Tests Passed: " + str(passed) + " Tests Failed: " + str(failed))
