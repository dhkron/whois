import pytz
import re
import dateutil.parser

from . import _parser


class Parser(_parser.Parser):
    '''
    '''
    supported_tlds = [
        'com',
        'net',
        'org',
    ]

    domain_not_exist_messages = [
        'No whois information found.',
        'Domain not found',
        'No such host is known.',
    ]
    extractors = {
        'creation_date': [
            {
                'match': {
                    'type': 'regex',
                    'values': [
                        re.compile(
                            pattern=r'(Creation|Created) Date: (?P<creation_date>.*)$',
                            flags=re.MULTILINE | re.IGNORECASE,
                        ),
                        re.compile(
                            pattern=r'created:[^\d\-]+(?P<creation_date>[\d\-]+)$',
                            flags=re.MULTILINE | re.IGNORECASE,
                        ),
                        re.compile(
                            pattern=r'\[Creation Date\](?P<creation_date>.+)$',
                            flags=re.MULTILINE | re.IGNORECASE,
                        ),
                    ],
                    'group_name': 'creation_date',
                    'normalizer': (
                        lambda creation_date_str: creation_date_str.strip()
                    ),
                },
                'converter': {
                    'type': 'function',
                    'value': (
                        lambda creation_date_str: dateutil.parser.parse(creation_date_str, fuzzy=True)
                    ),
                    'normalizer': (
                        lambda creation_date: creation_date.replace(tzinfo=None)
                    ),
                },
            },
        ],
        'updated_date': [
            {
                'match': {
                    'type': 'regex',
                    'values': [
                        re.compile(
                            pattern=r'(Updated|Update) Date: (?P<updated_date>.*)$',
                            flags=re.MULTILINE | re.IGNORECASE,
                        ),
                        re.compile(
                            pattern=r'\[Last Update\](?P<updated_date>.+)$',
                            flags=re.MULTILINE | re.IGNORECASE,
                        ),
                    ],
                    'group_name': 'updated_date',
                    'normalizer': (
                        lambda updated_date: updated_date.strip()
                    ),
                },
                'converter': {
                    'type': 'function',
                    'value': (
                        lambda updated_date_str: dateutil.parser.parse(updated_date_str, fuzzy=True)
                    ),
                    'normalizer': (
                        lambda updated_date: updated_date.replace(tzinfo=None)
                    ),
                },
            },
        ],
        'registrar': [
            {
                'match': {
                    'type': 'regex',
                    'values': [
                        re.compile(
                            pattern=r'Registrar: (?P<registrar>.*)$',
                            flags=re.MULTILINE | re.IGNORECASE,
                        ),
                    ],
                    'group_name': 'registrar',
                    'normalizer': (
                        lambda registrar: registrar.strip()
                    ),
                },
            },
        ],
        'registrant': [
            {
                'match': {
                    'type': 'regex',
                    'values': [
                        re.compile(
                            pattern=r'Registrant Organization: (?P<registrant>.*)$',
                            flags=re.MULTILINE | re.IGNORECASE,
                        ),
                        re.compile(
                            pattern=r'Organization: (?P<registrant>.*)$',
                            flags=re.MULTILINE | re.IGNORECASE,
                        ),
                    ],
                    'group_name': 'registrant',
                    'normalizer': (
                        lambda registrant: registrant.strip()
                    ),
                },
            },
        ],
    }
