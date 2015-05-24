#! /usr/bin/python

import os
loop = 1
collection = []

msg = '''
+-------------------------------+
|           Multi Dig           |
+-------------------------------+
|   Usage: Add domains per line |
|   type "dig" to dig           |
|   type "show" to show cache   |
|   type "clear" to clear cache |
|   type "exit" to quit         |
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

	elif query == 'exit':
		loop = 0
		print '[-]Bye Bye'

	elif query == 'clear':
		collection=[]
		os.system('clear')
		print msg
		print '[+]Cache cleared.\n'

	elif query == '?':
		if '?' in collection:
			collection.remove('?')
			print msg
