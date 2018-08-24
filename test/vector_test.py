import numpy
from numpy.ma import dot
v = [[1,2,3,4,5]]
w = [[10,20,30,40,50]]

nV = numpy.array(v)
nV = nV.reshape((5,1))
print(nV)
# print(dot(v, v))