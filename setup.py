import setuptools


setuptools.setup(
    name='whois',
    version='0.0.1',
    author='gal@intsights.com',
    author_email='gal@intsights.com',
    description=('A fast, simple, and comprehensive whois library'),
    zip_safe=True,
    install_requires=[
        'tldextract',
        'dateutil',
        'pytz',
    ],
    packages=setuptools.find_packages(),
)
