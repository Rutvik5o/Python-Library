#Joining numpy arrays

#vstack() => make a array vertically

import numpy as np

n1=np.array([19,5,35])

n2=np.array([5,63,66])

print(np.vstack((n1,n2)))

#hstack() => make a array horizontally

n3=np.array([10,20,39])

n4=np.array([40,50,70])


print(np.hstack((n3,n4)))

#column_stack() => first array as a column of 1st

n5=np.array([10,20,39])

n6=np.array([40,50,70])

n7=np.array([80,330,35])

print(np.column_stack((n5,n6,n7)))
