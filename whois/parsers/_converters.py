from . import converter


date_converters = [
    converter.DateRegex(
        pattern=r'(?P<day>[0-9]{1,2})[.\/ -](?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[.\/ -](?P<year>[0-9]{4}|[0-9]{2})',
    ),
    converter.DateRegex(
        pattern=r'[a-z]{3}\s(?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[.\/ -](?P<day>[0-9]{1,2})(\s+(?P<hour>[0-9]{1,2})[:.](?P<minute>[0-9]{1,2})[:.](?P<second>[0-9]{1,2}))?\s[a-z]{3}\s(?P<year>[0-9]{4}|[0-9]{2})',
    ),
    converter.DateRegex(
        pattern=r'[a-zA-Z]+\s(?P<day>[0-9]{1,2})(?:st|nd|rd|th)\s(?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December)\s(?P<year>[0-9]{4})',
    ),
    converter.DateRegex(
        pattern=r'(?P<year>[0-9]{4})[.\/-]?(?P<month>[0-9]{2})[.\/-]?(?P<day>[0-9]{2})(\s|T|/)((?P<hour>[0-9]{1,2})[:.-](?P<minute>[0-9]{1,2})[:.-](?P<second>[0-9]{1,2}))',
    ),
    converter.DateRegex(
        pattern=r'(?P<year>[0-9]{4})[.\/-]?(?P<month>[0-9]{2})[.\/-]?(?P<day>[0-9]{2})(\s|T|/)((?P<hour>[0-9]{1,2})[:.-](?P<minute>[0-9]{1,2})[:.-](?P<second>[0-9]{1,2}))',
    ),
    converter.DateRegex(
        pattern=r'(?P<year>[0-9]{4})[.\/-](?P<month>[0-9]{1,2})[.\/-](?P<day>[0-9]{1,2})',
    ),
    converter.DateRegex(
        pattern=r'(?P<day>[0-9]{1,2})[.\/ -]?(?P<month>[0-9]{1,2})[.\/ -]?(?P<year>[0-9]{4}|[0-9]{2})',
    ),
    converter.DateRegex(
        pattern=r'[a-z]* (?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (?P<day>[0-9]{1,2}).*(?P<year>[0-9]{4})',
    ),
    converter.DateRegex(
        pattern=r'(?P<day>[0-9]{1,2})-(?P<month>January|February|March|April|May|June|July|August|September|October|November|December)-(?P<year>[0-9]{4})',
    ),
    converter.DateRegex(
        pattern=r'(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})',
    ),
    converter.DateRegex(
        pattern=r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',
    ),
    converter.DateRegex(
        pattern=r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})T(?P<hour>[0-9]{2})[:.-](?P<minute>[0-9]{2})[:.-](?P<second>[0-9]{2})',
    ),
    converter.DateRegex(
        pattern=r'(?P<year>\d{4})\.\s?(?P<month>\d{2})\.\s?(?P<day>\d{2})\.?',
    ),
    converter.DateRegex(
        pattern=r'(?P<year>[0-9]{4})[./-]?(?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[./-]?(?P<day>[0-9]{1,2})',
    ),
    converter.DateRegex(
        pattern=r'(?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December) (?P<day>\d{2}) (?P<year>\d{4})',
    ),
    converter.DateRegex(
        pattern=r'(?P<year>\d{4})\-(?P<month>\d{2})\-(?P<day>\d{2})',
    ),
    converter.DateGeneric(),
]

registrar_converters = [
    converter.Dummy(),
]

registrant_converters = [
    converter.Dummy(),
]

email_converters = [
    converter.Dummy(),
]

domain_status_converters = [
    converter.Dummy(),
]

converters = {
    'creation_date': date_converters,
    'updated_date': date_converters,
    'expiration_date': date_converters,
    'registrar': registrar_converters,
    'registrant': registrant_converters,
    'abuse_email': email_converters,
    'domain_status': domain_status_converters,
}
