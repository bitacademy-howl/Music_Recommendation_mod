year = 2009
month = 11
page = "%s%s"% (year, month)
x = "asbss%s" % page
y = "asbss{0}".format(page)

print(y, type(y))
print(x, type(x))
print(page, type(page))