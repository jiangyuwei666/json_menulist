import menu
from lxml import etree

def getHow( html ) :#工艺
    s = etree.HTML( html )
    how = s.xpath( '//li[@class="w127"]//strong/text()')
    how_1 = how[ 0 ]
    how = s.xpath ( ' //li[@class="w127"]//a/text()')
    how_2 = how [ 0 ]
    how_final = how_1 + ":" +how_2
    return how_final#ok

def getTaste ( html ) :#口味
    s = etree.HTML( html )
    taste = s.xpath( '//li[@class="w127 bb0"]//strong/text()' )
    taste_1 = taste[0]
    taste = s.xpath ( ' //li[@class="w127 bb0"]//a/text()')
    taste_2 = taste[0]
    taste_final = taste_1 + ":" + taste_2
    return taste_final#ok

def getMakings ( html ) :#材料
    s = etree.HTML( html )
    makings= s.xpath( '//div[@class="yl fuliao clearfix"]//ul[@class="clearfix"]//li//h4//a/text()' )
    number = s.xpath( '//div[@class="yl fuliao clearfix"]//ul[@class="clearfix"]//li//span/text()' )
    makings_main_name = s.xpath ( '//div[@class="yl zl clearfix"]//ul[@class="clearfix"]//div[@class="c"]//h4//a/text()' )
    makings_main_number = s.xpath ( '//div[@class="yl zl clearfix"]//ul[@class="clearfix"]//div[@class="c"]//h4//span/text()' )
    makings_main_name = makings_main_name[ 0 ]
    makings_main_number = makings_main_number [ 0 ]
    makings_main = makings_main_name + ":" + makings_main_number
    for i in  range( len( makings ) ) :
        makings [ i - 1 ] = makings [ i - 1 ] + ":" + number [ i - 1 ]
    makings.append ( makings_main )
    return makings#ok

url = "http://www.meishij.net/zuofa/qingzhenghuanyu_2.html"
html = menu.getUrl( url )
print ( getHow( html ) )
print ( getTaste( html ) )
print ( getMakings( html ) )
