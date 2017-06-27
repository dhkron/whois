import setuptools


setuptools.setup(
    name='whois',
    version='0.1.6',
    author='gal@intsights.com',
    author_email='gal@intsights.com',
    description=('A fast, simple, and comprehensive whois library'),
    zip_safe=False,
    install_requires=[
        'Levenshtein',
        'lxml',
        'python-dateutil',
        'pytz',
        'requests',
        'tldextract',
    ],
    packages=setuptools.find_packages(),
    package_data={
        '': [
            'whois.exe',
            'whois_elf32',
        ],
    },
    include_package_data=True,
)
