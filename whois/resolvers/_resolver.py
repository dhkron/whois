class Resolver:
    name = ''

    @classmethod
    def get_raw_whois(
        cls,
        domain,
    ):
        raise NotImplementedError()

    @classmethod
    def normalize_raw_whois(
        cls,
        raw_whois,
    ):
        raise NotImplementedError()

    @classmethod
    def resolve(
        cls,
        domain,
    ):
        raw_whois = cls.get_raw_whois(
            domain=domain,
        )

        normalized_whois = cls.normalize_raw_whois(
            raw_whois=raw_whois,
        )

        return normalized_whois


class ResolverException(
    Exception,
):
    pass


class WhoisTimedOut(
    ResolverException,
):
    pass
