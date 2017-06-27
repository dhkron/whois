from . import resolvers


class Resolver:
    @staticmethod
    def resolve(
        domain,
        method='program',
    ):
        for resolver in resolvers.__resolvers__:
            if resolver.name == method:
                return resolver.resolve(
                    domain=domain,
                )

        raise Exception(
            'unknown resolver of method "{method}"'.format(
                method=method,
            )
        )
