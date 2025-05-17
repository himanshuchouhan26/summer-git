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


import csv

with open('Dataset_Malawi_National_Football_Team_Matches.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"Column 1: {row[0]}, Column 2: {row[1]}")

'''

import csv

data = [
    ['Name', 'Branch', 'Year', 'CGPA'],
    ['Nikhil', 'COE', 2, 9.0],
    ['Sanchit', 'COE', 2, 9.1],
    ['Aditya', 'IT', 2, 9.3],
    ['Sagar', 'SE', 1, 9.5],
    ['Prateek', 'MCE', 3, 7.8],
    ['Sahil', 'EP', 2, 9.1]
]

with open('Dataset_Malawi_National_Football_Team_Matches.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)