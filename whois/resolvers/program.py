import subprocess
import shlex
import os
import platform
import re
import stat

from . import _resolver


class Resolver(_resolver.Resolver):
    '''
    '''
    name = 'program'

    @classmethod
    def get_raw_whois(cls, domain):
        timeout = 10

        current_os = platform.system()
        current_architecture = platform.architecture()
        current_architecture_bits = current_architecture[0]
        if current_os == 'Linux':
            if current_architecture_bits == '64bit':
                program = os.path.abspath(
                    path=os.path.join(
                        os.path.dirname(__file__),
                        '../bin/whois_elf64',
                    )
                )
            else:
                program = os.path.abspath(
                    path=os.path.join(
                        os.path.dirname(__file__),
                        '../bin/whois_elf32',
                    )
                )

            if not os.access(program, os.X_OK):
                original_permissions = os.stat(program)
                os.chmod(program, original_permissions.st_mode | stat.S_IXGRP | stat.S_IXUSR | stat.S_IXOTH)
        elif current_os == 'Windows':
            program = os.path.abspath(
                path=os.path.join(
                    os.path.dirname(__file__),
                    '../bin/whois.exe',
                )
            )
        else:
            program = 'whois'

        command = '{program} {domain}'.format(
            program=program,
            domain=domain,
        )
        is_posix = os.name == 'posix'

        try:
            completed_process = subprocess.run(
                args=shlex.split(command, posix=is_posix),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired as exception:
            raise _resolver.WhoisTimedOut()

        output = completed_process.stdout
        whois_raw_data = output.decode(
            encoding='utf-8',
            errors='ignore',
        )
        stderr = completed_process.stderr
        error_string = stderr.decode(
            encoding='utf-8',
            errors='ignore',
        )

        if whois_raw_data == '' and error_string != '':
            raise _resolver.ErrorOccured(error_string)

        return whois_raw_data

    @classmethod
    def remove_program_banner(cls, raw_whois):
        '''
        '''
        raw_whois = re.sub(
            pattern='.*Mark Russinovich',
            repl='',
            string=raw_whois,
            flags=re.DOTALL,
        )
        raw_whois = re.sub(
            pattern='^Connecting to.*\.\.\.$',
            repl='',
            string=raw_whois,
            flags=re.MULTILINE,
        )

        return raw_whois

    @classmethod
    def normalize_raw_whois(cls, raw_whois):
        '''
        '''
        normalized_whois = raw_whois

        normalized_whois = normalized_whois.replace('\r\n', '\n')
        normalized_whois = cls.remove_program_banner(normalized_whois)
        normalized_whois = normalized_whois.strip()

        return normalized_whois
