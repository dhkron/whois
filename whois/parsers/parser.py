import re

from . import resources
from . import _matchers
from . import _converters


class Parser:
    '''
    '''
    domain_not_exist_patterns = resources.patterns.domain_not_exist_patterns

    has_no_whois_server_messages = [
        'no whois server',
    ]

    blocked_whois_request_messages = [
        'blacklist',
        'connection refused',
        'Network is unreachable',
    ]

    @classmethod
    def parse(cls, raw_whois):
        '''
        '''
        parsed_whois = {}

        has_whois_server = cls.has_whois_server(
            raw_whois=raw_whois,
        )
        if not has_whois_server:
            raise NoWhoisServer()

        is_domain_exist = cls.is_domain_exist(
            raw_whois=raw_whois,
        )
        if not is_domain_exist:
            raise DomainNotExists()

        is_blocked = cls.is_blocked(
            raw_whois=raw_whois,
        )
        if is_blocked:
            raise Blocked()

        creation_date = cls.extract_creation_date(
            raw_whois=raw_whois,
        )
        parsed_whois['creation_date'] = creation_date

        updated_date = cls.extract_updated_date(
            raw_whois=raw_whois,
        )
        parsed_whois['updated_date'] = updated_date

        expiration_date = cls.extract_expiration_date(
            raw_whois=raw_whois,
        )
        parsed_whois['expiration_date'] = expiration_date

        registrar = cls.extract_registrar(
            raw_whois=raw_whois,
        )
        parsed_whois['registrar'] = registrar

        registrant = cls.extract_registrant(
            raw_whois=raw_whois,
        )
        parsed_whois['registrant'] = registrant

        return parsed_whois

    @classmethod
    def is_blocked(cls, raw_whois):
        '''
        '''
        for blocked_whois_request_message in cls.blocked_whois_request_messages:
            if blocked_whois_request_message in raw_whois.lower():
                return True
        else:
            return False

    @classmethod
    def has_whois_server(cls, raw_whois):
        '''
        '''
        for has_no_whois_server_message in cls.has_no_whois_server_messages:
            if has_no_whois_server_message in raw_whois.lower():
                return False
        else:
            return True

    @classmethod
    def is_domain_exist(cls, raw_whois):
        '''
        '''
        for domain_not_exist_pattern in cls.domain_not_exist_patterns:
            if re.search(
                pattern=domain_not_exist_pattern,
                string=raw_whois.lower(),
                flags=re.IGNORECASE,
            ):
                return False
        else:
            return True

    @classmethod
    def extract_creation_date(cls, raw_whois):
        creation_date = cls.extract(
            attribute_name='creation_date',
            subject=raw_whois,
        )

        return creation_date

    @classmethod
    def extract_updated_date(cls, raw_whois):
        updated_date = cls.extract(
            attribute_name='updated_date',
            subject=raw_whois,
        )

        return updated_date

    @classmethod
    def extract_expiration_date(cls, raw_whois):
        expiration_date = cls.extract(
            attribute_name='expiration_date',
            subject=raw_whois,
        )

        return expiration_date

    @classmethod
    def extract_expiration_date(cls, raw_whois):
        expiration_date = cls.extract(
            attribute_name='expiration_date',
            subject=raw_whois,
        )

        return expiration_date

    @classmethod
    def extract_registrar(cls, raw_whois):
        registrar = cls.extract(
            attribute_name='registrar',
            subject=raw_whois,
        )

        if registrar:
            edited_registrar = resources.registrars.Registrars.get_registrar(
                subject=registrar,
            )

            return edited_registrar
        else:
            registrar = resources.registrars.Registrars.get_registrar(
                subject=raw_whois,
            )

        return registrar

    @classmethod
    def extract_registrant(cls, raw_whois):
        registrant = cls.extract(
            attribute_name='registrant',
            subject=raw_whois,
        )

        return registrant

    @classmethod
    def extract(cls, attribute_name, subject):
        '''
        '''
        match = None
        for matcher in _matchers.matchers[attribute_name]:
            match = matcher.match(subject)
            if not match:
                continue

            for converter in _converters.converters[attribute_name]:
                conversion = converter.convert(match)
                if not conversion:
                    continue

                return conversion

        return None


class ParserException(Exception):
    pass


class NoWhoisServer(ParserException):
    pass


class DomainNotExists(ParserException):
    pass


class Blocked(ParserException):
    pass
