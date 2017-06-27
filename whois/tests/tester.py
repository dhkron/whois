# import querier
# import tldextract
# import traceback


# def check_domain(domain):
#     try:
#         tld = tldextract.extract(domain)
#         q = whois.querier.Querier()
#         try:
#             result = querier.Querier().query(domain.rstrip())
#         except querier.NoWhoisServer:
#             print("NoWhoisServer " + domain.rstrip())
#             return
#         except querier.DomainNotExists:
#             print("DomainDoesNotExist. " + domain.rstrip())
#             return
#         except querier.ParsingError:
#             print('Bad Domain. No creation_date and no updated_date ' + domain.rstrip())
#             return
#         except querier.Blocked:
#             print('Blocked: ' + domain.rstrip())
#             return
#         except querier.WhoisTimedOut:
#             print('WhoisTimeout: ' + domain.rstrip())
#             return
#         except querier.DomainNotExists:
#             print('Domain does not exists' + domain.rstrip())
#             return
#         if not result['raw_whois']:
#             print("Bad Domain. A raw key was not present. " + domain.rstrip())

#         try:
#             print("Good Domain. " + domain.rstrip() + " " + result['creation_date'].strftime("%d/%m/%y"))
#         except Exception as ex:
#             if result['updated_date']:
#                 print("Good Domain With Updated Date Only. " + domain.rstrip() + " " + result['updated_date'].strftime("%d/%m/%y"))
#             else:
#                 print("Bad Domain. Not time given. " + domain.rstrip())
#     except Exception as ex:
#         traceback.print_exc()
#         if "has no whois server" in str(ex):
#             print("Skipped domain. " + tld.suffix)
#         else:
#             print("Bad Domain. Who Is did not succeed. " + domain.rstrip())

# if "__main__" == __name__:
#     # res = []
#     # template = '''matcher.Regex(
#     #         pattern=r%tmp%,
#     #         group='value',
#     #         flags=re.IGNORECASE,
#     #     ),'''
#     # registrants = [name.strip() for name in open('/home/uri/registrant')]
#     # for reg in registrants:
#     #     res.append(template.replace('%tmp%', reg))
#     # print('finshed')
#     check_domain('www.google.com')
