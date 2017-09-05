#ok
import requests
from lxml import etree

def getUrl ( url ) :
    try :
        html = requests.get( url )
        html.encoding = 'utf-8'
    except Exception as e :
        print ("open error")
    return html.text

def getUrlList ( html ) :
    s = etree.HTML( html )
    List = s.xpath ('//div[@class="listtyle1"]//a//@href')
    return List

def AllList ( page , meal ) :
    menu = []
    for i in range( page ) :
        url = "http://www.meishij.net/chufang/diy/"+str ( meal ) + "/?&page="+ str  ( i )
        list_new = getUrlList( getUrl( url ) )
        menu = menu + list_new
    return menu

