#==> Number intersection & difference

print("Intersect id=> common values on both arrays")

import numpy as np

n1=np.array([10,20,30])

n2=np.array([40,50,30])

print(np.intersect1d(n1,n2))

print("set differ id=> show that array which present in one array and not present in second array")

print(np.setdiff1d(n1,n2))

print(np.setdiff1d(n2,n1))

print("Addition of numpy arrays")

print(np.sum([n1,n2]))

print(np.sum([n1,n2],axis=0))

print(np.sum([n1,n2],axis=1))

