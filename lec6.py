'''
import pandas as pd

a=pd.Series([1,233,67,90])
print(a)
type(a)


a={
   "Name": ['Sam', 'Raj', 'Rahul', 'Gaurav'],
   "Domain": ['D.E', 'D.S', 'D.S', 'Full Stack'],
   "Duration": [30,15,45,30]
}
df=pd.DataFrame(a)
print(df)


import pandas as pd
df = pd.read_csv("D:\\summer-regex\\google.csv")
print(df) 

'''

import pandas as pd
df = pd.read_csv("D:\\summer-regex\\makemytrip.csv")
print(df) 