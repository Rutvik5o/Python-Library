print("Numpay Save & Load")

import numpy as np

n1=np.array([10,20,30,40,50,70])

print(np.save('my_numpy',n1)) #=> save numpy array on my_numpy

n2=np.load('my_numpy.npy') #=> Loading numpay array

print(n2)