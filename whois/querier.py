import tldextract
import os
import tempfile

from . import parser
from . import resolver


class Querier:
    '''
    '''
    def __init__(self):
        self.whois_resolver = resolver.Resolver()
        self.whois_parser = parser.Parser()

        self.tldextract = tldextract.tldextract.TLDExtract(
            os.path.join(
                tempfile.gettempdir(),
                'tld_extract_data',
            ),
        )

    def get_domain_parts(self, domain):
        domain_extracted = self.tldextract(domain)

        domain_part = domain_extracted.domain
        suffix_part = domain_extracted.suffix

        if not domain_extracted.suffix or not domain_extracted.domain:
            return None

        return {
            'domain': domain_part,
            'suffix': suffix_part,
        }

    def query(self, domain):
        '''
        '''
        domain_parts = self.get_domain_parts(
            domain=domain,
        )

        if not domain_parts:
            raise DomainIsInvalid()

        raw_whois = self.whois_resolver.resolve(
            domain=domain,
        )

        parsed_whois = self.whois_parser.parse(
            domain_parts=domain_parts,
            raw_whois=raw_whois,
        )

        return {
            'raw_whois': raw_whois,
            'parsed': parsed_whois,
        }


class WhoisResolverException(Exception):
    pass


class DomainIsInvalid(WhoisResolverException):
    pass
