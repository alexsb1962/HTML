
import urllib.request as ul
from lxml import etree

url = 'http://www.google.ru'
u = ul.urlopen(url)
doc = u.read()
doc='<root>data</root>'
print( doc )
tree = etree.fromstring(doc)
print(etree.tostring( tree, pretty_print = True) )

