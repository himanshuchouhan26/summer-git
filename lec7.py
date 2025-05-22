
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("D:\\summer-regex\\titanic.csv")
'''
print(df) 
print(df.head())
print(df.tail(3))
print(df.sample(3))
print(df.shape)
print(df.columns)  # it will returns column names
print(df[2:5])
print(df.loc[2:5, ["Survived","Pclass"]])  #row range  and column name ..... in this last values will be included
print(df.iloc[2:5, :3])  # row range  and column range
print(df.dtypes)
print(df.isnull())
print(df.isnull().sum())  # it will calculate total number off missing values in each column
p=df.dropna() # it will remove missing rows
print(p.isnull().sum())
print(df.drop(columns = ["Cabin"]))
df['Fare']= df['Fare'].fillna(5)
df['Age']= df['Age'].fillna(10)
print(df.head)
df['Fare'] = df['Fare'].astype(int)
print(df['Fare'].dtype)
df['Survived'].value_counts()
df=df.rename(columns={'Age':'Updated_Age'})
print(df)

# Data
# (1). continous data => we can divide in more sub data . ex. Date_of_birth, river_length , weight
# (2). Discrete data => we cannot divide in more sub-data.
# (3). Ex. Marital status , total_number_of_employees_in a_company

# Exploratory Data Analysis
# (1). Univariate Analysis => analysis on one column 
# (2). Bivariate Analysis => analysis on two column
# (3). Multivariate Analysis => analysis on more than two column

# Numerical => histogram,linechart
# Categorical => pie chart ,bar chart, countplot

sns.countplot(x = df['Survived'])
df['Survived'].value_counts()
df['Survived'].value_counts().plot(kind = 'bar')
df['Survived'].value_counts().plot(kind = 'pie', autopct = '%.2f')

plt.hist(x = df['Survived'])
plt.hist(x = df['Age'])
plt.show()
sns.boxplot(x = df['Survived'])

df = pd.read_csv("D:\\summer-regex\\tips.csv")
print(df)
df.head(3)
'''
sns.scatterplot(x = df['total_bill'],y=df['tips'])