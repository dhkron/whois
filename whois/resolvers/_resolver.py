class Resolver:
    '''
    '''
    name = ''

    @classmethod
    def get_raw_whois(cls, domain):
        raise NotImplemented()

    @classmethod
    def normalize_raw_whois(cls, whois_data):
        '''
        '''
        raise NotImplemented()

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
