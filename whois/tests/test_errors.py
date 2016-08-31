from .. import querier

import unittest


class TestCase(unittest.TestCase):
    def test_invalid_domain(self):
        whois_querier = querier.Querier()

        self.assertRaises(
            querier.InvalidDomain,
            whois_querier.query,
            'kjlasdnflkjandsf.asdfasdf.asdf'
        )

    def test_blocked(self):
        whois_querier = querier.Querier()

        block_raised = False
        for i in range(10):
            try:
                whois_querier.query('google.fr')
            except querier.Blocked:
                block_raised = True
        self.assertTrue(block_raised)
