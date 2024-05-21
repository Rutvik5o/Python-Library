import pandas as pd

s1=pd.read_csv('ex1.csv')

print("Mean")

print(s1.mean())

print("Minimum")

print(s1.min())

print("Median")

print(s1.median())

print("Maximum")

print(s1.max())

print("Apply Method")

print("apply method basically work on a different column so if i want to perform a same function on the different columns of a pandas dataframe that is when i will go ahead and use the apply method")

def half(s):
    return s*0.5;  #=> making value to its half

s2=s1[['Height','Weight']].apply(half)

print(s2)

print("Value_counts()")  #=> show the frequency of a data value 

s3=s1['Weight'].value_counts()

print(s3)

print("sort_values()") #=> for sort to data with a respect to a particular column then we will use i


s4=s1.sort_values(by='Height')

print(s4)


