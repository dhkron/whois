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

        completed_process = None
        try:
            completed_process = subprocess.run(
                args=shlex.split(command, posix=is_posix),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired as exception:
            raise _resolver.WhoisTimedOut()

        if completed_process:
            output = completed_process.stdout

        whois_raw_data = output.decode('utf-8', errors='ignore')

        process_timed_out = completed_process is None

        return {
            'whois_data': whois_raw_data,
            'timed_out': process_timed_out,
        }

    @classmethod
    def remove_program_banner(cls, whois_data):
        '''
        '''
        whois_data = re.sub(
            pattern='.*Mark Russinovich',
            repl='',
            string=whois_data,
            flags=re.DOTALL,
        )
        whois_data = re.sub(
            pattern='^Connecting to.*\.\.\.$',
            repl='',
            string=whois_data,
            flags=re.MULTILINE,
        )

        return whois_data

    @classmethod
    def normalize_raw_whois(cls, whois_data):
        '''
        '''
        normalized_whois = whois_data

        normalized_whois = normalized_whois.replace('\r\n', '\n')
        normalized_whois = cls.remove_program_banner(normalized_whois)
        normalized_whois = normalized_whois.strip()

        return normalized_whois

    @classmethod
    def resolve(cls, domain):
        '''
        '''
        raw_whois = cls.get_raw_whois(
            domain=domain,
        )

        normalized_whois = cls.normalize_raw_whois(
            whois_data=raw_whois['whois_data'],
        )

        return normalized_whois
