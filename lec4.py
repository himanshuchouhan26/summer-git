'''
 class HouseDesign:
  color="yellow"
 h1=HouseDesign()
 print(h1.color)

 h2=HouseDesign()
 h2.color="white"
 print(h2.color)


 class HouseDesign:
  def __init__(self):
   print("Mistri sahab aa gaye")
  color="yellow"

 h1=HouseDesign()


class HouseDesign:
 def __init__(self,x):
  self.color=x

h1=HouseDesign("green")
print("h1:",h1.color)

h2=HouseDesign("pink")
print("h2:",h2.color)


#inheritence => parent class => child class
#10lakh =>
#10lakh + khud ke pass

class parent:
 amount=50000

class child(parent):
 salary=10000

c1=child()
 print(c1.amount)

class Driver:
 def __init__(self,id,name,email):
  self.id=id
  self.name=name
  self.email=email

d1=Driver(1,"suresh","suresh@gmial.com")
print(d1.id,d1.name,d1.email)

d2=Driver(2,"ramesh","ramesh@gmail.com")
print(d2.id,d2.name,d2.email)


class customer:
 def __init__(self,x,y,z):
  self.x=x
  self.y=y
  self.z=z

c1=customer(202,"dharmesh","dharmesh@gmail.com")
print(c1.x,c1.y,c1.z)


class Customer(Driver):
 def __init__(self,a,b,c):
  super().__init__(a,b,c)

c1=Customer(12,"sakshi","sakshi@gmail.com")
print(c1.name)

'''

class employee:
 def __init__(self,name,email,salary):
  self.name=name
  self.email=email
  self.salary=salary

 def info(self):
  print(self.salary //12 ,self.email.split("@")[-1])
 
e1=employee("abhishek","abhi@gmail.com",60000)
e1.info()