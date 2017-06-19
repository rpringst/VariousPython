import requests
from bs4 import BeautifulSoup

def getID(objID):
	r = requests.get('http://services.runescape.com/m=itemdb_rs/Logs/viewitem?obj=' + str(objID))
	soup = BeautifulSoup(r.content, "html.parser")
	print('Item: ' + soup.title.string)
	print('Price: ' + soup.h3.span.string)

mainLoop = True

while mainLoop:
	objID = None
	while not objID:
	    try:
	        objID = int(raw_input('Input the object ID: '))
	    except ValueError:
	        print 'Invalid Number!'
	getID(objID) 
	if str(raw_input('Find another price? y/n ')) == 'n':
		mainLoop = False
