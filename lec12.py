'''
## LogisticRegression ---> when we have categorical target column .

## Backend ---> Activation function ---> sigmoid --->
## probability convert all sub categories ---> 
## threshhold_value = 0.5

#0.5 <= output = 1
#0.5 < output = 0

## install UV 
## what is the difference between UV and PIP 

import numpy as np 
import pandas as pd

df = pd.read_csv("D:\\summer-regex\\covid_toy.csv")
print(df.head(3))
df.isnull().sum()

from sklearn.impute import SimpleImputer

si = SimpleImputer()

df['fever'] = si.fit_transform(df[['fever']])

# df.isnull().sum()
print(df.head(3))

from sklearn.preprocessing import LabelEncoder

lb = LabelEncoder()

df['gender'] = lb.fit_transform(df['gender'])
df['cough'] = lb.fit_transform(df['cough'])
df['city'] = lb.fit_transform(df['city'])
df['has_covid'] = lb.fit_transform(df['has_covid'])
print(df.head(2))

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


## Decision Tree Classifier --->
## Changes in entropy and gini index

# -p1Log1-p2Log2  ## if we have 2 sub-categories
# -p1Log1-p2Log2-p3Log3....-pnLogn  ### if we have more than 2 sub-categories

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()
from sklearn.model_selection import train_test_split
dt.fit(x_train , y_train)

y_pred = dt.predict(x_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test , y_pred)) 




## RandomForestClassifier

## Ensemble method ---> multiple decision trees works ---> 100 d.t. --->70 yes , 30 No ---> final output ---> majority(yes)


from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()

rf.fit(x_train , y_train)
y_pred = rf.predict(x_test)
print(accuracy_score(y_test , y_pred))



# LinearRegression ---DecisionTreeRegreesion ---> RF

import numpy as np
import pandas as pd

df = pd.read_csv( "D:\\summer-regex\\insurance.csv")

print(df.head(3))

df.isnull().sum()

df = pd.get_dummies(df , columns = ['sex' , 'smoker' , 'region'])
print(df.head(3))

x = df.drop(columns = ['charges'])

y = df['charges'] 

from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state = 42)


from sklearn.linear_model import LinearRegression

lr = LinearRegression()

print(lr.fit(x_train , y_train))

y_pred = lr.predict(x_test)

from sklearn.metrics import r2_score

print(r2_score(y_test , y_pred))

## DecisionTreeRegression

from sklearn.tree import DecisionTreeRegressor

dt = DecisionTreeRegressor()
from sklearn.model_selection import train_test_split
dt.fit(x_train , y_train)

y_pred = dt.predict(x_test)

print(r2_score(y_test , y_pred))

## RandomForestRegressor

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor()
from sklearn.model_selection import train_test_split
rf.fit(x_train , y_train)

y_pred = rf.predict(x_test)

print(r2_score(y_test , y_pred))

'''

## Naive-Bayes-Classifier


import numpy as np 
import pandas as pd

df = pd.read_csv("D:\\summer-regex\\Social_Network_Ads.csv" , usecols = ['Age' , 'EstimatedSalary' , 'Purchased'])
print(df.head(3))
df.isnull().sum()






































