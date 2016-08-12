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
            raise InvalidDomain()

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

        try:
            raw_whois = self.resolver.resolve(
                domain=domain,
                method=method,
            )
        except resolvers._resolver.WhoisTimedOut:
            raise WhoisTimedOut(
                raw_whois='',
            )

        try:
            parsed_whois = self.whois_parser.parse(
                raw_whois=raw_whois,
            )
        except parsers.parser.DomainNotExists:
            raise DomainNotExists(
                raw_whois=raw_whois,
            )
        except parsers.parser.NoWhoisServer:
            raise NoWhoisServer(
                raw_whois=raw_whois,
            )
        except parsers.parser.Blocked:
            raise Blocked(
                raw_whois=raw_whois,
            )

        if parsed_whois['creation_date'] is None and parsed_whois['updated_date'] is None:
            if domain_parts['suffix'] not in _config.partial_data_tlds:
                raise ParsingError(
                    raw_whois=raw_whois,
                )

        whois_result = {}
        whois_result.update(parsed_whois)
        whois_result['raw'] = raw_whois

        return whois_result


class WhoisResolverException(Exception):
    def __init__(self, raw_whois):
        self.raw_whois = raw_whois


class ParsingError(WhoisResolverException):
    pass


class DomainNotExists(WhoisResolverException):
    pass


class NoWhoisServer(WhoisResolverException):
    pass


class Blocked(WhoisResolverException):
    pass


class WhoisTimedOut(WhoisResolverException):
    pass


class InvalidDomain(WhoisResolverException):
    pass
