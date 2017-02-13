'''
    Created on: 2/3/2017
    This stand alone function is used to blah blah blah>

'''

import urllib

URL_TYPE = "utf8"

def convertString2Dictionary(inputString = ""):
    errorDict = {'error':'true'}
    return errorDict
    
    
def isValidInput(inputString = ""):
	url=urllib.unquote(inputString).decode(URL_TYPE)
	print url
	

