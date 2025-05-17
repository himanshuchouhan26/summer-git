'''
#dictionary => Data type
#Key value
#key => unique identifier
#value=> unique/duplicate
#dictionary is mutable
#no index position


mydictionary={10:"Himanshu", 20:"Chouhan"}
mydictionary[10]="Ishaan"  #update the value
mydictionary["amount"]=1000  #insert the value

print(mydictionary)
mydictionary.pop(20)
print(mydictionary)

print(help(mydictionary))

mydictionary.keys()
mydictionary.value()

data="hello"
count=0
for char in data:
 count+=1
mydictionary={"total":count}
print(mydictionary)


data="user"
mydictionary={}
for char in data:
 mydictionary[char]=1
print(mydictionary)


data="hey isha"
mydictionary={}
for char in data:
 if char in "aeiou":
  mydictionary[char]=1
print(mydictionary)

mydictionary={"amount":15}
mydictionary["amount"]= mydictionary["amount"]+200
print(mydictionary)


data="hey ishaeea"
mydictionary={}
for char in data:
 if char in "aeiou":
  if char not in mydictionary:
   mydictionary[char]=1
  else:
   mydictionary[char]= mydictionary[char]+1
print(mydictionary)


#list comprehension

[i+5 for i in [10,20,30,40,50] ]
   

{char:1 for char in "hey"}


#Function => set of statement => task to perform
#logic => code reusability

a=100  #global variable
def test():
 z=19 # local variable
 print("hello",z,a)


def msg(username):  #parameter
 print("hey user",username)

msg("Himanshu")


def totalsum(num):
 total=0
 for i in range(1,num+1):
  total=total+i
 print(f"Sum of {num} is =>",total)


def pattern(n):
 for i in range(1, n + 1):
   for j in range(1,i):
       print('-',end="")
   
   for k in range(1,n-i+2):
      print(k,end="")
   print("")
                                   

def func(a,b):
 print("a=>",a , "b=>",b)

func()

'''

