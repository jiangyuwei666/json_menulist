import requests
import os
import urllib.request
from lxml import etree

def getUrl ( url ) :
    try :
        html = requests.get( url )
        html.encoding = 'utf-8'
    except Exception as e :
        print ("open error")
    return html.text

def setPath ( name ) :
    pass

def getDownload( urls , path ) :
    count = 0
    for i in urls :
        pass