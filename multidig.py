#! /usr/bin/python

import os

loop = 1
collection = []

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


msg = '''
+-------------------------------+
|           Multi Dig           |
+-------------------------------+
|   Usage: Add domains per line |
|                               |
|   Supported commands:         |
|   type "dig"   - dig list     |
|   type "show"  - show list    |
|   type "clear" - clear list   |
|   type "whois" - whois list   |
|   type "exit"  - quit         |
|   type "?"	 - help menu    |
+-------------------------------+
'''
print msg

while loop != 0:
    query = raw_input('# ')
    collection.append(query)
    if query == 'dig':
        if 'dig' in collection:
            collection.remove('dig')
        print '----------RESPONSE----------'
        for x in collection:
            print '\n----------'+x.upper()+'----------'
            print '[+]A records for ' + x + bcolors.WARNING
            os.system('dig a ' + x + ' +short')
            print bcolors.ENDC + '[+]MX records for '+x+bcolors.WARNING
            os.system('dig mx ' + x + ' +short')
            print bcolors.ENDC + '[+]NS records for '+x+bcolors.WARNING
            os.system('dig ns ' + x + ' +short')
            print bcolors.ENDC + '[+]TXT records for '+x+bcolors.WARNING
            os.system('dig txt ' + x + ' +short')
            print bcolors.ENDC
    elif query == 'show':
        if 'show' in collection:
            collection.remove('show')
        print '[+]Displaying current list:\n'
        for x in collection:
            print x
        print '\n[+]Done.'

    elif query == 'exit':
        loop = 0
        print '[-]Bye Bye'

    elif query == 'whois':
        if 'whois' in collection:
            collection.remove('whois')
        for x in collection:
            print '\n\n[+]Initiating whois search on '+x
            os.system('whois ' + x)
            print '[+]Whois search done for domain:'+x
            raw_input(':enter')
        print '[+]End of list.'

    elif query == 'clear':
        collection = []
        os.system('clear')
        print msg
        print '[+]List cleared.\n'

    elif query == '?':
        if '?' in collection:
            collection.remove('?')
        print msg
