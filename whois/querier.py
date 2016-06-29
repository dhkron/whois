import tldextract
import os
import tempfile

from . import parser
from . import resolver


class Querier:
    '''
    '''
    def __init__(self):
        self.whois_parser = parser.Parser()
        self.resolver = resolver.Resolver()

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

    def query(self, domain, method="program"):
        '''
        '''
        raw_whois = self.resolver.resolve(
            domain=domain,
            method=method,
        )

        parsed_whois = self.whois_parser.parse(
            raw_whois=raw_whois,
        )

        if 'is_domain_exist' in parsed_whois and not parsed_whois['is_domain_exist']:
            raise DomainDoesNotExist()

        if 'has_whois_server' in parsed_whois and not parsed_whois['has_whois_server']:
            raise WhoIsServerDoesNotExist()

        if 'is_blocked' in parsed_whois and parsed_whois['is_blocked']:
            raise BlockedWhoisRequest()

        if parsed_whois['creation_date'] is None and parsed_whois['updated_date'] is None:
            raise CannotParse()

        return {
            'raw_whois': raw_whois,
            'parsed': parsed_whois,
        }


class WhoisResolverException(Exception):
    pass


class DomainIsInvalid(WhoisResolverException):
    pass


class CannotParse(WhoisResolverException):
    pass


class DomainDoesNotExist(WhoisResolverException):
    pass


class WhoIsServerDoesNotExist(WhoisResolverException):
    pass


class BlockedWhoisRequest(WhoisResolverException):
    pass
