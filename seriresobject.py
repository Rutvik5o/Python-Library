import pandas as pd

#=> Series Object is one-dimensional labeled array

s1=pd.Series([1,2,3,4,5])

print(s1)

'''

li=[1,2,4,5]

s2=pd.Series(li)

print(s2)

'''
#=> given your own index
s3=pd.Series([9,8,7,6,5],index=['a','b','c','d','e'])

print(s3)

#=> you can also create a series object from a dictionary!!

s4=pd.Series({'a':100,'b':200,'c':300})

print(s4)

#=> you can change the index position

s5=pd.Series({'a':100,'b':200,'c':400},index=['b','c','d','a'])

print(s5)

#=> Extractng Individual elements

s6=pd.Series([1,2,3,4,5,6,7])

print(s6[6])

#=> Extracting a sequence of elements

print(s6[:4])

#=> Extracting elements from back

print(s6[-3:])  #=> extract elements from back so we use - operator.

print("Adding a scaler value to Series Elemenets")

print(s1+5)

print("Subtraction")

print(s1-100)

print("Multiplication")

print(s1*5)

print("Adding two series object")

print("Printing both object\n", s1,"\n",s6)

print(s1+s6)





