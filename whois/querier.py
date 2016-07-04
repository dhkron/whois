import tldextract
import os
import tempfile

from . import _config
from . import parser
from . import resolver

from . import parsers
from . import resolvers


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

    def query(self, domain, method='program'):
        '''
        '''
        domain_parts = self.get_domain_parts(
            domain=domain,
        )

        raw_whois = self.resolver.resolve(
            domain=domain,
            method=method,
        )

        try:
            parsed_whois = self.whois_parser.parse(
                raw_whois=raw_whois,
            )
        except parsers.parser.DomainNotExists:
            raise DomainNotExists()
        except parsers.parser.NoWhoisServer:
            raise NoWhoisServer()
        except parsers.parser.Blocked:
            raise Blocked()

        if parsed_whois['creation_date'] is None and parsed_whois['updated_date'] is None:
            if domain_parts['suffix'] not in _config.partial_data_tlds:
                raise ParsingError()

        return {
            'raw_whois': raw_whois,
            'parsed': parsed_whois,
        }


class WhoisResolverException(Exception):
    pass


class ParsingError(WhoisResolverException):
    pass


class DomainNotExists(WhoisResolverException):
    pass


class NoWhoisServer(WhoisResolverException):
    pass


class Blocked(WhoisResolverException):
    pass
