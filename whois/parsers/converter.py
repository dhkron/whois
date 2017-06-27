import re
import dateutil.parser


class DateRegex:
    def __init__(
        self,
        pattern,
    ):
        self.pattern = pattern

    def convert(
        self,
        date_string,
    ):
        match = re.search(
            pattern=self.pattern,
            string=date_string,
            flags=re.IGNORECASE,
        )

        if not match or not match.groups():
            return None

        try:
            year = match.group('year')
            month = match.group('month')
            day = match.group('day')
        except Exception:
            return None

        try:
            date_object = dateutil.parser.parse(
                timestr='{day} {month} {year}'.format(
                    day=day,
                    month=month,
                    year=year,
                ),
                dayfirst=True,
            )

            return date_object.replace(
                tzinfo=None,
            )
        except:
            return None


class DateGeneric:
    def __init__(
        self,
    ):
        pass

    def convert(
        self,
        date_string,
    ):
        try:
            date_object = dateutil.parser.parse(
                timestr=date_string,
                fuzzy=True,
            )

            return date_object.replace(
                tzinfo=None,
            )
        except:
            return None


class Dummy:
    def __init__(
        self,
    ):
        pass

    def convert(
        self,
        original_string,
    ):
        return original_string
