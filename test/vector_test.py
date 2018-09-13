import numpy
from numpy.ma import dot
v = [[1,2,3,4,5,6]]
w = [[10,20,30,40,50,60]]

nV = numpy.array(v)
nV1 = nV.reshape((3,2))
nV2 = nV.reshape((3,2),order='F')
print('---------nv1 : order :none---------','\n', nV1,'\n','---------nv1 : order : "F" ---------','\n', nV2)
# print(dot(v, v))