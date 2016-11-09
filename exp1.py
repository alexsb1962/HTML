
import urllib.request as ul
from lxml import html

#url = 'file://localhost//d://py//expr//test.html'
url = 'http://www.google.ru'
u = ul.urlopen(url)
doc = u.read()
u.close()

tree = html.fromstring(doc)
lt=list(tree)
with open('data.html',mode='w') as f:
    print(html.tostring(tree),file=f)


def walk(tree):
    for elem in list(tree):
        print(elem.tag )
        walk(elem)
    return tree        
    
ls=walk(tree)

#print(html.tostring( tree, pretty_print = True) )

