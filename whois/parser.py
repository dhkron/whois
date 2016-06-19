from . import parsers


class Parser:
    '''
    '''
    def __init__(self):
        pass

    def parse(self, raw_whois, domain_parts):
        '''
        '''
        for parser in parsers.__parsers__:
            if domain_parts['suffix'] not in parser.supported_tlds:
                continue

            parsed_data = parser.parse(raw_whois)

            if parsed_data:
                return parsed_data

        return None
