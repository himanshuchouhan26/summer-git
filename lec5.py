'''
# data science
# problem => Data acquire => Data pre-process => data storage
# Data preparation => data analysis => data visualize 
# ML and algorithm (chatbot,open ai service,open cv,NLP) => Data report

# python =>  libraries => pandas and numpy
# numpy => numerical python
# scientific library => data in form nd array  (n dimentional array)
# [1,2,3,4]
#  [1,2],
#  [3,4]
# data prepare in form of number 


import numpy
type (numpy.arange(7))


import numpy as np
arr1= np.arange(5)
arr1

arr1=np.array([1,2,3])
arr1.size

arr1=np.array([[1,2],[3,4],[5,6]])
print(arr1.size)
print(arr1.shape)

arr2=np.arange(3)
print(arr2.shape)

arr1=np.array([[1.0,2],[3,4],[5,6]])
print(arr1.size)
print(arr1.shape)
print(arr1.dtype)

np.ones([3,4])

arr1=np.arange(9)
arr1.reshape(3,3)

import numpy as np
a=np.array([[1,2],[3,4]])
print(a)

b=a.transpose()
print(b)

arr1=np.array([[[1.0,2],[2,3],[5,6]]])
arr1.ndim

arr1=np.array([[[1.0,2],[2,3],[5,6]]])
arr1.ndim
arr2.shape

#NUMPY
# string => convert => int

#Pandas : powerful => data transform, clean , prepare
# series : 1D array
# Dataframe : collection of series tabular format for your data

import pandas 
pandas.Series([10,2,34,4])

import pandas as pd
series=pd.Series([10,2,34,4])
series.values


import pandas as pd
series1=pd.Series([10,2,34,4])
series1.values
series1.index
print(series1[0])
series1[0]=90    
series1[5]=1000
series1
series1.max()
series1.idmax()
series1.max()
print(series1.idmax())

import pandas as pd
series1=pd.Series(([10,2,34,4]), index=["A","B","C","D"])
series.to_dict

arr1=np.array([10,13,15,19,24])
series1=pd.series(arr1)
series1
type(series)


arr1=np.array([10,13,15,19,24])
series1=pd.Series(arr1)
series1.value_counts()




arr1=np.array([10,13,15,19,24])
series1=pd.Series(arr1)
series.is_unique()

series1.nunique()

arr1=np.array([10,13,15,19,24])
series1=pd.Series(arr1)
series.value_counts(ascending=True)



arr1=np.array([10,13,15,19,24,10,15])
series1=pd.Series(arr1)
series1.drop_duplicates()
series1.drop_duplicates(inplace=True)


arr1=np.array([10,13,15,19,24,10,15])
series1.values
series1.index
series1.max()
series1.idmax()
series1.max()
print(series1.idmax())
series.to_dict




data=[ [10,12,13],[13,14,15] ]
pd.DataFrame(data)
df=pd.DataFrame(data,columns=['Product1','Product2','Product3'])
type(df['Product1'])




#1. read a csv file in pandas and select 1 column and count how many time the value is present here
#2. count how many number of unique value you have
#3. drop the duplicates values from the column 
#4. change the integer  column to float sum float datatype

'''


import pandas as pd
df = pd.read_csv("D:\\summer-regex\\ml-latest-small\\ratings.csv")
print(df) 




#1. count how many movie and tv show are present in this dataset
#2. count for each year how many number of movies releases
#3. from september to october month how many actions movies are released
#4. find out the number of movies and tv shows release for each year









