import numpy as np
import pandas as pd
'''
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv("D:\\summer-regex\\covid_toy.csv")

print(df.head(3))
df.isnull().sum()

from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(df.drop(columns = ['has_covid']) , df['has_covid'] , test_size = 0.2)
print(x_train)

#adding simple imputer to fever column

si = SimpleImputer(strategy = "mean")
x_train_fever = si.fit_transform(x_train[['fever']])

#also the test data

x_test_fever = si.fit_transform(x_test[['fever']])
print(x_train_fever.shape)


#Ordinal Encoding => cough

oe = OrdinalEncoder(categories = [['Mild' , 'Strong']])
x_train_cough = oe.fit_transform(x_train[['cough']])

#also the test data
x_test_cough = oe.fit_transform(x_test[['cough']])
print(x_train_cough.shape)


# OneHotEncoding => Gender , city

ohe = OneHotEncoder(drop = 'first' , sparse_output = False)
x_train_gender_city = ohe.fit_transform(x_train[['gender' , 'city']])

#also the test data
x_test_gender_city = ohe.fit_transform(x_test[['gender' , 'city']])
print(x_train_gender_city.shape)


# Extracting Age
x_train_age = x_train.drop(columns = ['gender' , 'fever' , 'cough' , 'city']).values

#also the tast data

x_test_age = x_test.drop(columns = ['gender' , 'fever' , 'cough' , 'city']).values
print(x_train_age.shape)

x_train_transformed = np.concatenate((x_train_age , x_train_fever , x_train_gender_city , x_train_cough) , axis = 1)
print(x_train_transformed.shape)


from sklearn.compose import ColumnTransformer  # this is how to import ColumnTransformer

transformer = ColumnTransformer(transformers=[('tnf1',SimpleImputer(),['fever']),     #in a 'fever' column by the help of SI we fill missing values by mean , median , mode.
('tnf2',OrdinalEncoder(categories=[['Mild','Strong']]),['cough']),  # by this process we encode the data.
('tnf3',OneHotEncoder(sparse_output=False,drop='first'),['gender','city'])
],remainder='passthrough')  # remainder = passthrough ==> it means rest all the columns remain same.
print(transformer.fit_transform(x_train).shape)


# ML Models => 
# Data  --- we will train the model ---> we pass input data to our model and this model will return
# prediction of that input data



#ML Models 
# (1). Supervised ML Model ---> when we have labelled data , then we will use this model will return
# (2). UnSupervised ML Model ---> when we have only values not included column name


#(1). Supervised ML Models :
# (1). Linear Regression --->  when we have target data as Numerical(Continuous)

df = pd.read_csv("D:\\summer-regex\\insurance.csv")
print(df)

df.isnull().sum()

df = pd.get_dummies(df , columns = ['sex' , 'smoker' , 'region'])
print(df.head(3))

x = df.drop(columns = ['charges'])  ### Input features
y = df['charges']  ### Target features

from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state = 42)


from sklearn.linear_model import LinearRegression

lr = LinearRegression()  ### this is a model and we use when we have numerical target data

print(lr.fit(x_train , y_train))

y_pred = lr.predict(x_test)

from sklearn.metrics import r2_score
print(r2_score(y_test , y_pred))
'''


# (2). LogisticRegression ---> when we have categories 

df=pd.read_csv("D:\\summer-regex\\covid_toy.csv")
df=df.dropna()
print(df.head(3))

df=pd.get_dummies(df,columns=['gender','cough','city'])

from sklearn.preprocessing import LabelEncoder

lb=LabelEncoder()

df['has_covid'] = lb.fit_transform(df['has_covid'])

x=df.drop(columns=['has_covid'])
y=df['has_covid']
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state = 42)


from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()
lr.fit(x_train,y_train)

y_pred=lr.predict(x_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test,y_pred))











































