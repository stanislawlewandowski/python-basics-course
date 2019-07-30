marketing = ['loyality program', 'client promotion', 'market research']
marketing.append('public relations')
print(marketing[1])
marketing.insert(1, 'investor relations')
print(marketing)
emailMarketing = marketing.copy()
emailMarketing.sort()
print(emailMarketing)
internalEmails = ['internal communication']
emailMarketing.extend(internalEmails)
emailTuple = tuple(emailMarketing)
print(emailTuple)
print(emailMarketing)