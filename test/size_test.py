import sys
from encodings.utf_8_sig import encode

print(len('1F하'))

print(sys.getsizeof('k'))
print(sys.getsizeof('1'))
print(sys.getsizeof('12'))

a = '하이'
b = 'hi'

c = a.encode('utf-8')
print(c, len(c))

print(len(a.encode('utf-8')))
print(len(b.encode('utf-8')))

print(sys.getsizeof('fuck'))
