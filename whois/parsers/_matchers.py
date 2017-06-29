import re

from . import matcher


matchers = {
    'creation_date': [
        matcher.Regex(
            pattern=r'\[Created on\]\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Created on[.]*: [a-zA-Z]+, (?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Creation Date:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Creation date\s*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registration Date:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Created Date:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Created on:\.*\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Created on\s?[.]*:\s?(?P<value>.+)\.',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Date Registered\s?[.]*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Domain Created\s?[.]*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Domain registered\s?[.]*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Domain record activated\s?[.]*:\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Record created on\s?[.]*:?\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Record created\s?[.]*:?\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Created\s?[.]*:?\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registered on\s?[.]*:?\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registered\s?[.]*:?\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Domain Create Date\s?[.]*:?\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Domain Registration Date\s?[.]*:?\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'created:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'\[Registered Date\]\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'created-date:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Domain Name Commencement Date: (?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'registered:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'registration:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registration Time:\s(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'created:\s+(?P<value>\d+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registered Date\s+: (?P<value>.*)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Fecha de Creación: (?P<value>.*)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registered:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Date de creation#[\.|\s]*(?P<value>.*)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'First registration date:\s(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Data de registo / Creation Date \(dd/mm/yyyy\):\s(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'activated on:\s+(?P<value>.*)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Fecha de registro[:]?\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Date de creation[:]?\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Fecha de Creacion[:]?\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Activation:\.*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'domain_dateregistered[:]?\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'record created[:]?\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
    ],
    'expiration_date': [
        matcher.Regex(
            pattern=r'paid-till:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'expiration_date:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'expire-date:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'renewal:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'expire:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Domain Expiration Date\s?[.]*:?\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'expires at:\s+(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Expired\s?[.]*:?\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Expire Date\s?[.]*:?\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Expires\s?[.]*:?\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Record expires\s?[.]*:?\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Record expires on\s?[.]*:?\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Domain expires\s?[.]*:\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Record will expire on\s?[.]*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Domain Currently Expires\s?[.]*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Expiry\s*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Exp(?:iry)? Date\s?[.]*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Expires on\s?[.]*:\s?(?P<value>.+)\.',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Expires on:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Expiration date\s*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Expiration Date:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Expires on[.]*: [a-zA-Z]+, (?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrar Registration Expiration Date:[ ]*(?P<value>.+)-[0-9]{4}',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'\[Expires on\]\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Fecha de Vencimiento:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Data de expiração / Expiration Date \(dd/mm/yyyy\):\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Fecha de expiración \(Expiration date\): (?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
    ],
    'updated_date': [
        matcher.Regex(
            pattern=r'\[Last Updated\]\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Record modified on[.]*: (?P<value>.+) [a-zA-Z]+',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Record last updated on[.]*: [a-zA-Z]+, (?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Updated Date:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Updated date\s*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Record last updated on\s?[.]*:?\s?(?P<value>.+)\.',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Domain record last updated\s?[.]*:\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Domain Last Updated\s?[.]*:\s*?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Last updated on:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Date Modified\s?[.]*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Last Modified\s?[.]*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Domain Last Updated Date\s?[.]*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Record last updated\s?[.]*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Modified\s?[.]*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'changed:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'last_update:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Last Update\s?[.]*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Last updated on (?P<value>.+) [a-z]{3,4}',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Last updated:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'last-updated:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'\[Last Update\]\s*(?P<value>.+) \([A-Z]+\)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Updated\s?[.]*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Last-update\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Derniere modification:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'domain_datelastmodified:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
    ],
    'registrar': [
        matcher.Regex(
            pattern=r'registrar:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'registrar_name:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrar:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Sponsoring Registrar Organization:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Sponsoring Registrar:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registered through:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrar Name[.]*:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Record maintained by:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registration Service Provided By:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrar of Record:\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Domain Registrar :\s?(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registration Service Provider: (?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'\tName:\t\s(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrar Name:\s+(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
    ],
    'registrant': [
        matcher.Regex(
            pattern=r'    Registrant:\n        (?P<value>.+)\n\n',
            group='value',
            flags=re.IGNORECASE | re.MULTILINE,
        ),
        matcher.Regex(
            pattern=r'Registrant Organization:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'reg-name:\s*(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Owner OrgName : (?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Organisation: (?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'   Registrant:[ ]*\n      (?P<value>.*)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrant:\n  (?P<value>.+)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'(?:Registrant Organization:(?P<value>.*)\n)?',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrant Organization:(?P<value>.*)?',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrant Organization: (?P<value>.+)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrant\n(?:    (?P<value>.+)\n)?',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r' Registrant Contact Details:[ ]*\n    (?P<value>.*)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'(?:owner-organization:[ ]*(?P<value>.*)\n)?',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrant:\n registrant_org: (?P<value>.*)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Holder of domain name:\n(?P<value>[\S\s]+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Contact Information:\n\[Name\]\s*(?P<value>.*)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'g\. \[Organization\]               (?P<value>.+)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrant Organization:(?P<value>.*)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Organization:     (?P<value>.+)\n?',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r' Organisation Name[.]* (?P<value>.*)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Eligibility Name:[ ]*(?P<value>.+)\n[\s\S]*',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrant:[ ]*(?P<value>.+)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Domain Owner:\n\t(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrant: (?P<value>.+)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'registrant-organization:\s*(?P<value>.*)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrant Contact Information :[ ]*\n[ ]+.*\n[ ]+.*\n[ ]+(?P<value>.*)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Contact Information : For Customer # [0-9]+[ ]*\n[ ]+.*\n[ ].*\n[ ]+(?P<value>.*)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrant:\n   Name:           (?P<value>.+)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'   Registrant:\n      (?P<value>.+)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Domain Holder: (?P<value>.+)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'   Registrant:\n      (?P<value>.+)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrant:\n(?P<value>.+)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrant Contact Information:\n\nCompany English Name \(It should be the same as the registered/corporation name on your Business Register Certificate or relevant documents\):(?P<value>.+)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrant Organization:(?P<value>.*)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Organization Using Domain Name\n Organization Name\.+:(?P<value>.*)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'owner:\s+(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'org:\s+(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrant                  : (?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'    Registrant:\n\n        Name:(?P<value>.+)        ',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'Registrant Contact Name:\s+(?P<value>.+)',
            group='value',
            flags=re.IGNORECASE,
        ),
    ],
    'abuse_email': [
        matcher.Regex(
            pattern=r'Registrar Abuse Contact Email: (?P<value>.+)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'trouble:\s+Spam:\s*mailto:(?P<value>.+)\n',
            group='value',
            flags=re.IGNORECASE,
        ),
    ],
    'domain_status': [
        matcher.Regex(
            pattern=r'Domain Status: *?(?P<value>[a-z]+?)(:? .+)?\n',
            group='value',
            flags=re.IGNORECASE,
        ),
        matcher.Regex(
            pattern=r'   Status: *?(?P<value>[a-z]+?)(:? .+)?\n',
            group='value',
            flags=re.IGNORECASE,
        ),
    ],
}

'''
abuse_email -> trouble:\s+Spam:\s*mailto:(?P<value>.+)\n -> jcbressources.fr, queried 2017-05-29
'''
