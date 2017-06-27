from . import parsers


class Parser:
    @classmethod
    def parse(
        cls,
        raw_whois,
    ):
        parsed_data = parsers.parser.Parser.parse(raw_whois)

        if parsed_data:
            return parsed_data

        return None

    @classmethod
    def has_error(
        cls,
        raw_whois,
    ):
        error_string = parsers.parser.Parser.has_error(raw_whois)

        return error_string
