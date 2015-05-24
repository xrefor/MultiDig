#! /usr/bin/python

import os
loop = 1
collection = []

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
|   type "?"	 - help menu 
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
			print '\n\n----------'+x.upper()+'----------'
			print '[+]A records for '+x
			os.system('dig a '+x+' +short')
			print '\n[+]MX records for '+x
			os.system('dig mx '+x+' +short')
			print '\n[+]NS records for '+x
			os.system('dig ns '+x+' +short')
			print '\n[+]TXT records for '+x
			os.system('dig txt '+x+' +short')
	elif query == 'show':
		if 'show' in collection:
			collection.remove('show')
		print '[+]Displaying current list:'
		for x in collection:
			print x
		print '[+]Done.'

	elif query == 'exit':
		loop = 0
		print '[-]Bye Bye'

	elif query == 'whois':
		if 'whois' in collection:
			collection.remove('whois')
		for x in collection:
			print '\n\n[+]Initiating whois search on '+x
			os.system('whois '+x)
			print '[+]Whois search done for domain:'+x
			raw_input(':enter')
		print '[+]End of list.'

	elif query == 'clear':
		collection=[]
		os.system('clear')
		print msg
		print '[+]List cleared.\n'

	elif query == '?':
		if '?' in collection:
			collection.remove('?')
		print msg
