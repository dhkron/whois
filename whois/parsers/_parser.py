from . import resources


class Parser:
    '''
    '''
    @classmethod
    def parse(cls, raw_whois):
        '''
        '''
        parsed_whois = {}

        is_domain_exist = cls.is_domain_exist(
            raw_whois=raw_whois,
        )
        parsed_whois['is_domain_exist'] = is_domain_exist

        is_blocked = cls.is_blocked(
            raw_whois=raw_whois,
        )
        parsed_whois['is_blocked'] = is_blocked

        creation_date = cls.extract_creation_date(
            raw_whois=raw_whois,
        )
        parsed_whois['creation_date'] = creation_date

        updated_date = cls.extract_updated_date(
            raw_whois=raw_whois,
        )
        parsed_whois['updated_date'] = updated_date

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
        return False

    @classmethod
    def is_domain_exist(cls, raw_whois):
        '''
        '''
        for domain_not_exist_message in cls.domain_not_exist_messages:
            if domain_not_exist_message in raw_whois['whois_data']:
                return False

        return True

    @classmethod
    def extract_creation_date(cls, raw_whois):
        creation_date = cls.extract(
            attribute_name='creation_date',
            subject=raw_whois['whois_data'],
        )

        return creation_date

    @classmethod
    def extract_updated_date(cls, raw_whois):
        updated_date = cls.extract(
            attribute_name='updated_date',
            subject=raw_whois['whois_data'],
        )

        return updated_date

    @classmethod
    def extract_registrar(cls, raw_whois):
        registrar = cls.extract(
            attribute_name='registrar',
            subject=raw_whois['whois_data'],
        )

        if not registrar:
            registrar = resources.registrars.Registrars.get_registrar(
                raw_whois=raw_whois['whois_data'],
            )

        return registrar

    @classmethod
    def extract_registrant(cls, raw_whois):
        registrant = cls.extract(
            attribute_name='registrant',
            subject=raw_whois['whois_data'],
        )

        return registrant

    @classmethod
    def extract(cls, attribute_name, subject):
        '''
        '''
        for extractor in cls.extractors[attribute_name]:
            match = cls.match(
                pattern=extractor['match'],
                subject=subject.replace('\r\n','\n'),
            )

            if not match:
                continue

            if 'converter' not in extractor:
                return match

            converted_value = cls.convert(
                pattern=extractor['converter'],
                subject=match,
            )

            if converted_value:
                return converted_value

        return None

    @classmethod
    def match(cls, pattern, subject):
        '''
        '''
        if pattern['type'] == 'regex':
            for compiled_regex in pattern['values']:
                match = compiled_regex.search(subject)
                if not match:
                    continue

                matched_value = match.group(pattern['group_name'])
                if 'normalizer' not in pattern:
                    return matched_value

                normalized_value = pattern['normalizer'](matched_value)

                return normalized_value

        return None

    @classmethod
    def convert(cls, pattern, subject):
        '''
        '''
        if pattern['type'] == 'function':
            converted_string = pattern['value'](subject)
            if 'normalizer' not in pattern:
                return converted_string

            normalized_value = pattern['normalizer'](converted_string)

            return normalized_value

        return None
