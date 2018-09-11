from modules.collection.urlMaker import UrlMaker, URL_Node

a = UrlMaker('track', 101010122)

print(a)

a.set_param(URL_Node.TRACK, 11112)
print(a)

b = UrlMaker.set_param(a, 1010, 20202)
print(a)

a.set_param(node=110101)
print(a)