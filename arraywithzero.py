import numpy as np

n1=np.zeros((1,2))

n2=np.zeros((10,10))

print(n1)

print(n2)


#you can also intialize with a particular number

n3=np.full((10,10),10)  #2nd parameter is what value you want to intialize

print(n3)

n4=np.full((5,3),1)

print(n4)

#intialize numpy array within a range


n5=np.arange(10,200)  #=> not include 200

print(n5)

n6=np.arange(10,105,5)

print(n6)

#initializing numpy array with random numbers

n7=np.random.randint(1,100,6) #=> 3rd parameter is how much number you want

print(n7)

n8=np.array([[1,2,3],[4,5,6]]) #-> shape of the array

print(n8)

print(n8.shape)

n8.shape=(3,2) #=> changing the shape of the array  

print(n8)