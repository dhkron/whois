import re
import os


class Registrars:
    '''
        https://www.icann.org/registrar-reports/accredited-list.html
    '''
    registrars = []

    @classmethod
    def get_registrar(
        cls,
        subject,
    ):
        '''
        '''
        if not getattr(cls, 'registrars'):
            with open(os.path.join(os.path.dirname(__file__), 'registrars_names')) as registrars_names_file:
                original_names = registrars_names_file.readlines()

            cls.registrars = [
                registrar
                for registrar in [
                    {
                        'original': original_name.strip(),
                        'edited': re.sub(
                            pattern='[^\d\w]',
                            repl='',
                            string=original_name,
                        ).lower(),
                    }
                    for original_name in original_names
                ]
                if len(registrar['edited']) > 4
            ]

        edited_subject = re.sub(
            pattern='[^\d\w]',
            repl='',
            string=subject,
        )
        edited_subject = edited_subject.lower()

        for registrar in cls.registrars:
            if edited_subject in registrar['edited'].lower():
                return registrar['original']

        return None
