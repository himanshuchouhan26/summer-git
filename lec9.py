'''
# introduction to machine learning
# Data => divide (input , target) => trained by ML model => ML model data prediction => 
# Model Accuracy 


# Normal Distribution => 
# -3 -2 -1 0 1 2 3
# Here 0 => Central tendancy(Mean , Median)
# Gap(standard deviation)equal
# why we convert our data into Normal Distribution
# (1). Calculation easy 
# (2). take less time for training and executing

# ML => Feature Engineering (create Appropriate data) + ML models => solution
# Feature Engineering

# (1). Data Dividation

import numpy as np 
import pandas as pd
df = pd.read_csv("D:\\summer-regex\\covid_toy.csv")
print(df)
print(df.head(3))
df.isnull().sum() ### return total missing values in a dataframe

from sklearn.impute import SimpleImputer
si=SimpleImputer() #it will fill missing values

df['fever'] = si.fit_transform(df[['fever']])
print(df.head())

df['gender'].value.counts() # it will return total frequency of each sub category in a column 
df['gender']=df['gender'].map({"Female":0 , "Male":1})
df['cough'].value.counts()
df['cough']=df['cough'].map({"Mild":0 , "Strong":1})
df['city'].value.counts()
df['has covid'].value.counts()
df['city']=df['city'].map({
       "Kolkata":0,
       "Banglore":1,
       "Delhi":2,
       "Mumbai":3
})
df['has covid']=df['has covid'].map({"No":0 , "Yes":1})
df.sample(3)
x = df.drop(columns = ['has_covid']) ### Independent data
print(x)
y = df['has_covid'] ### Target/dependant data
'''
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
						    test_size=0.2,
						    random_state=42)

print("Total Data Shape :" , df.shape) 
print("-------------------------------") 
print("Input Data Shape :" , x.shape) 
print("x_train Data Shape :" , x_train.shape) 
print("x_test Data Shape :" , x_test.shape) 

print("Input Data Shape :" , y.shape) 
print("y_train Data Shape :" , y_train.shape) 
print("y_test Data Shape :" , y_test.shape) 
print("-------------------------------") 











