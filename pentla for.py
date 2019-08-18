data = ['Error:File cannot be open', 'Error:No free space on disk','Error:File missing',
        'Warning:Internet connection lost', 'Error:Access denied']
for error in data:
    elements = error.split(':')
    print(elements[0].upper())
    print(elements[1])

print('----------------')

