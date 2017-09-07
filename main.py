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
    path = r"D:/H5_new//" + str ( name )
    try :
        os.mkdir( path )
    except:
        print ( "error" )
    return path

def getDownload( urls , path , name ) :
    count = 1
    for url in urls :
        filename = os.path.join( path ,  str( name ) + str ( count ) + ".jpg" )
        try:
            urllib.request.urlretrieve( url , filename )
        except:
            print( "download error" )
