import requests
from bs4 import BeautifulSoup

mainLoop = True

while mainLoop:
	objID = None
	while not objID:
	    try:
	        objID = int(raw_input('Input the object ID: '))
	    except ValueError:
	        print 'Invalid Number!'
	r = requests.get('http://services.runescape.com/m=itemdb_rs/Logs/viewitem?obj=' + str(objID))
	soup = BeautifulSoup(r.content, "html.parser")
	
	print('Item: ' + soup.title.string.strip(' - Grand Exchange - RuneScape'))
	print('Price: ' + soup.h3.span.string)
	exitValue = None
	while not exitValue:
	    try:
	        exitValue = str(raw_input('Find another price? y/n '))
	    except ValueError:
	        print 'Invalid Input!'
	if exitValue == 'n':
		mainLoop = False
	
