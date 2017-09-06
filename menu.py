#ok
import main
from lxml import etree

def getUrlList ( html ) :
    s = etree.HTML( html )
    List = s.xpath ('//div[@class="listtyle1"]//a//@href')
    return List

def AllList ( page , meal ) :
    menu = []
    for i in range( page ) :
        url = "http://www.meishij.net/chufang/diy/"+str ( meal ) + "/?&page="+ str  ( i )
        list_new = getUrlList( main.getUrl( url ) )
        menu = menu + list_new
    return menu