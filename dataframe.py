#import pandas as pd

p=pd.DataFrame({"Name":['abc','xyz','nmp'],"Marks":[73,65,35]})

print(p)

#=>inbuilt functions

print("head")

s2=pd.read_csv('ex.csv')

print(s2.head()) #=> it will be show only first 5 data

print(s2.tail()) #=> it will be show only last 5 data

#for see how many columns and rows in data frame

print(s2.shape)

#=> showing mean values & many more

print(s2.describe()) 

print("Extract individual rows and columns")

print(".iloc would help us to extract rows and columns with respect to their index.")

print(s2.iloc[0:3,0:2]) #=>rows,columns => 0:3 in 3 exclusive,0:2 in 2 exclusive

print("loc=> method in over here for the column section, so we can't really give index value over here and we had to give in the name of the columns.")

print(s2.loc[1:5,("Name","Occupation")])


print("Dropping the columns")

print(s2.drop('Age',axis=1)) #=>asis value 0 represent => rows , value 1 represent => Columns

print("Dropping the rows")

print(s2.drop([1,2,3],axis=0))




