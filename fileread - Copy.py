'''
f = open("user.txt","w")
#print(f.read())
f.write("ishaan")
f.close

# read and write dono krne he toh (r+) use hoga

f = open("abc.txt","r+")
print(f.read())
f.write("Japan")
f.close
'''

import csv

with open('Dataset_Malawi_National_Football_Team_Matches.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"Column 1: {row[0]}, Column 2: {row[1]}")