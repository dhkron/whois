import tldextract
import subprocess
import shlex
import tempfile
import os

from . import parser


class Resolver:
    '''
    '''
    def __init__(self):
        self.tldextract = tldextract.tldextract.TLDExtract(
            os.path.join(tempfile.gettempdir(), 'tld_extract_data'),
        )
        self.whois_parser = parser.Parser()

    def get_raw_whois(self, domain, program='whois'):
        timeout = 10
        command = '{program} {domain}'.format(
            program=program,
            domain=domain,
        )

        completed_process = None
        try:
            completed_process = subprocess.run(
                args=shlex.split(command),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired as exception:
            output = exception.output

        if completed_process:
            output = completed_process.stdout

        whois_raw_data = output.decode('utf-8', errors='ignore')
        whois_raw_data = whois_raw_data.replace('\r\n', '\n')

        process_timed_out = completed_process is None
        process_error = process_timed_out or (completed_process and completed_process.returncode == 0)

        return {
            'whois_data': whois_raw_data,
            'timed_out': process_timed_out,
            'error': process_error,
        }

    def get_domain_parts(self, domain):
        domain_extracted = self.tldextract(domain)

        domain_part = domain_extracted.domain
        suffix_part = domain_extracted.suffix

        if not domain_extracted.suffix or not domain_extracted.domain:
            return None

        return {
            'domain': domain_part,
            'suffix': suffix_part,
        }

    def query(self, domain):
        '''
        '''
        domain_parts = self.get_domain_parts(
            domain=domain,
        )

        if not domain_parts:
            raise DomainIsInvalid()

        raw_whois = self.get_raw_whois(
            domain=domain,
        )

        parsed_whois = self.whois_parser.parse(
            domain_parts=domain_parts,
            raw_whois=raw_whois,
        )

        return {
            'raw_whois': raw_whois,
            'parsed': parsed_whois,
        }


class WhoisResolverException(Exception):
    pass


class DomainIsInvalid(WhoisResolverException):
    pass
