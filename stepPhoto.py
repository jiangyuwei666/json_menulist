import  main
from lxml import etree

def getPhotoUrl ( html ) :#步骤照片
    s = etree.HTML( html )
    PhotoList= s.xpath ( '//div[@class="content clearfix"]//div[@class="c"]//p//img//@src')
    return PhotoList#ok

url = "http://www.meishij.net/zuofa/yangcongxianrouhuntun_1.html"
html = main.getUrl( url )
print ( getPhotoUrl( html ) )