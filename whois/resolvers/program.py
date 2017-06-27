import subprocess
import shlex
import os
import platform
import re
import stat
import select
import time

from . import _resolver


class Resolver(
    _resolver.Resolver,
):
    name = 'program'

    @classmethod
    def get_raw_whois(
        cls,
        domain,
    ):
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

        raw_whois = cls.get_command_output(
            command=command,
            is_posix=is_posix,
            timeout=10,
        )

        return raw_whois

    @classmethod
    def get_command_output(
        cls,
        command,
        is_posix,
        timeout=10,
    ):
        process = None
        all_output = ''
        start_time = time.time()

        try:
            poller = select.epoll()

            process = subprocess.Popen(
                args=shlex.split(
                    s=command,
                    posix=is_posix,
                ),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )

            poller.register(process.stdout, select.EPOLLHUP | select.EPOLLIN)

            while start_time + timeout > time.time():
                for fileno, event in poller.poll(
                    timeout=1,
                ):
                    if event & select.EPOLLHUP:
                        poller.unregister(
                            fd=fileno,
                        )

                        break

                    output = process.stdout.read()
                    output = output.decode(
                        encoding='utf-8',
                        errors='ignore',
                    )
                    all_output += output

                try:
                    process.wait(0)

                    break
                except subprocess.TimeoutExpired:
                    pass
        finally:
            if process is not None:
                process.terminate()

                try:
                    os.waitpid(
                        process.pid,
                        0,
                    )
                except ChildProcessError:
                    pass

                output = process.stdout.read()
                output = output.decode(
                    encoding='utf-8',
                    errors='ignore',
                )
                all_output += output

                try:
                    process.kill()
                except ProcessLookupError:
                    pass

        empty_whois_result = all_output.strip() == ''
        timedout_whois_result = all_output.strip() == 'Interrupted by signal 15...'

        if empty_whois_result or timedout_whois_result:
            raise _resolver.WhoisTimedOut()
        else:
            return all_output.strip()

    @classmethod
    def remove_program_banner(
        cls,
        raw_whois,
    ):
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
    def normalize_raw_whois(
        cls,
        raw_whois,
    ):
        normalized_whois = raw_whois

        normalized_whois = normalized_whois.replace('\r\n', '\n')
        normalized_whois = cls.remove_program_banner(normalized_whois)
        normalized_whois = normalized_whois.strip()

        return normalized_whois
