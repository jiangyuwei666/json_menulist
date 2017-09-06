from lxml import  etree

def getStep ( html ) :
    s = etree.HTML( html )
    step = s.xpath ( '//div[@class="content clearfix"]//div[@class="c"]//p/text()')
    for i in range( len ( step ) ):
        step[ i ] = str ( i + 1  )  +"." + step [ i ]
    return step
#ok
