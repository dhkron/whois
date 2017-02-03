import re


domain_not_exist_patterns = [
    re.compile(
        pattern=r'.*?domain not found.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?no such host is known..*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?no match for.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?No whois information found\..*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?No Data Found.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?nothing found.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?No entries found.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?ERROR:101: no entries found.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?No data was found to match the request criteria\..*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?Domain Status: No Object Found.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?The requested domain was not found.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?query_status: 220 Available.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?Domain not found.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?NOT FOUND.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?No Object Found.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?Not found: [\w\d\-\.]+.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?No information available about domain name.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?The queried object does not exist.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?does not exist in database.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?no existe.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?Status: free.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?No Match.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?[\w\d\-\.]+ is free.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?domain name not known.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?Status:\s*AVAILABLE.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?Domain [\w\d\-\.]+ is available for purchase.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?this server does not have .* any data for [\w\d\-\.]+.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?Object_Not_Found.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?The domain has not been registered.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?Status: Not Registered.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?-7: %Invalid pattern.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?We do not have an entry in our database matching your query.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?No Found.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?%ERROR:103: Domain is not registered.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?% Not Registered.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?name or service not known.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
]

blocked_whois_request_patterns = [
    re.compile(
        pattern=r'.*?blacklist.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?WHOIS LIMIT EXCEEDED.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?connection refused.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?network is unreachable.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?lookup quota exceeded.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?your request could not be performed\..*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?connection reset by peer.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?the number of requests per client per time interval.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?you have exceeded this limit.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?please slow down and try again later\..*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?blacklisted: you have exceeded the query limit for your network or ip address.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?Too many requests\.\.\..*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?queries per hour exceeded for your network.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?we will permanently block access from this network if queries continue.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?maximum query rate reached.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?please maintain at least 10-second time before starting another enquiry.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?You exceeded the maximum allowable number of whois lookups.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?No further queries can be done.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?You have reached configured rate limit.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
    re.compile(
        pattern=r'.*?Domain is not available or is reserved by the registry.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
]

has_no_whois_server_patterns = [
    re.compile(
        pattern=r'.*?no whois server.*?',
        flags=re.IGNORECASE | re.MULTILINE,
    ),
]
