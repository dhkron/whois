from . import resources
from . import _matchers
from . import _converters


class Parser:
    domain_not_exist_patterns = resources.patterns.domain_not_exist_patterns
    blocked_whois_request_patterns = resources.patterns.blocked_whois_request_patterns
    has_no_whois_server_patterns = resources.patterns.has_no_whois_server_patterns

    @classmethod
    def parse(
        cls,
        raw_whois,
    ):
        parsed_whois = {}

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

        parsed_whois['additional'] = {}

        abuse_email = cls.extract_abuse_email(
            raw_whois=raw_whois,
        )
        parsed_whois['additional']['abuse_email'] = abuse_email

        domain_status = cls.extract_domain_status(
            raw_whois=raw_whois,
        )
        parsed_whois['additional']['domain_status'] = domain_status

        return parsed_whois

    @classmethod
    def has_error(
        cls,
        raw_whois,
    ):
        has_whois_server = cls.has_whois_server(
            raw_whois=raw_whois,
        )
        if not has_whois_server:
            return 'no_whois_server'

        is_domain_exist = cls.is_domain_exist(
            raw_whois=raw_whois,
        )
        is_blocked = cls.is_blocked(
            raw_whois=raw_whois,
        )

        if not is_domain_exist and is_blocked:
            return 'domain_not_exists_or_blocked'

        if not is_domain_exist:
            return 'domain_not_exists'

        if is_blocked:
            return 'blocked'

        return 'no_error'

    @classmethod
    def is_blocked(
        cls,
        raw_whois,
    ):
        for blocked_whois_request_pattern in cls.blocked_whois_request_patterns:
            if blocked_whois_request_pattern.findall(
                string=raw_whois,
            ):
                return True

        return False

    @classmethod
    def has_whois_server(
        cls,
        raw_whois,
    ):
        for has_no_whois_server_pattern in cls.has_no_whois_server_patterns:
            if has_no_whois_server_pattern.findall(
                string=raw_whois,
            ):
                return False

        return True

    @classmethod
    def is_domain_exist(
        cls,
        raw_whois,
    ):
        for domain_not_exist_pattern in cls.domain_not_exist_patterns:
            if domain_not_exist_pattern.findall(
                string=raw_whois,
            ):
                return False

        return True

    @classmethod
    def extract_creation_date(
        cls,
        raw_whois,
    ):
        creation_date = cls.extract(
            attribute_name='creation_date',
            subject=raw_whois,
        )

        return creation_date

    @classmethod
    def extract_updated_date(
        cls,
        raw_whois,
    ):
        updated_date = cls.extract(
            attribute_name='updated_date',
            subject=raw_whois,
        )

        return updated_date

    @classmethod
    def extract_expiration_date(
        cls,
        raw_whois,
    ):
        expiration_date = cls.extract(
            attribute_name='expiration_date',
            subject=raw_whois,
        )

        return expiration_date

    @classmethod
    def extract_registrar(
        cls,
        raw_whois,
    ):
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
    def extract_registrant(
        cls,
        raw_whois,
    ):
        registrant = cls.extract(
            attribute_name='registrant',
            subject=raw_whois,
        )

        return registrant

    @classmethod
    def extract_abuse_email(
        cls,
        raw_whois,
    ):
        abuse_email = cls.extract(
            attribute_name='abuse_email',
            subject=raw_whois,
        )

        return abuse_email

    @classmethod
    def extract_domain_status(
        cls,
        raw_whois,
    ):
        domain_status = cls.extract_all(
            attribute_name='domain_status',
            subject=raw_whois,
        )

        domain_status_set = set(domain_status)

        return list(domain_status_set)

    @classmethod
    def extract(
        cls,
        attribute_name,
        subject,
    ):
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

    @classmethod
    def extract_all(
        cls,
        attribute_name,
        subject,
    ):
        matches = None
        for matcher in _matchers.matchers[attribute_name]:
            matches = matcher.finditer(subject)
            if not matches:
                continue

            for match in matches:
                for converter in _converters.converters[attribute_name]:
                    conversion = converter.convert(match)
                    if not conversion:
                        continue

                    yield conversion

                    break

        return None


class ParserException(
    Exception,
):
    pass


class NoWhoisServer(
    ParserException,
):
    pass


class DomainNotExists(
    ParserException,
):
    pass


class Blocked(
    ParserException,
):
    pass
