import re
import os
import Levenshtein


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

        most_close_registrar = ''
        most_close_registrar_distance_ratio = 0
        for registrar in cls.registrars:
            registrar_distance_ratio = Levenshtein.ratio(
                edited_subject,
                registrar['edited'],
            )
            if registrar_distance_ratio > most_close_registrar_distance_ratio:
                most_close_registrar = registrar['original']
                most_close_registrar_distance_ratio = registrar_distance_ratio

        return most_close_registrar
