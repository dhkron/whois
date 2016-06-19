import re
import os


class Registrars:
    '''
        https://www.icann.org/registrar-reports/accredited-list.html
    '''
    @staticmethod
    def get_registrar(raw_whois):
        '''
        '''
        if not getattr(Registrars, 'registrars', None):
            with open(os.path.join(os.path.dirname(__file__), 'registrars_names')) as registrars_names_file:
                original_names = registrars_names_file.readlines()

            Registrars.registrars = [
                registrar
                for registrar in [
                    {
                        'original': original_name.strip(),
                        'edited': re.sub('[^\d\w]', '', original_name).lower(),
                    }
                    for original_name in original_names
                ]
                if len(registrar['edited']) > 4
            ]

        edited_raw_whois = re.sub('[^\d\w]', '', raw_whois)
        edited_raw_whois = edited_raw_whois.lower()

        for registrar in Registrars.registrars:
            if registrar['edited'].lower() in edited_raw_whois:
                return registrar['original']

        return None
