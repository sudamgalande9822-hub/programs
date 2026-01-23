# age = int(input("enter age = "))
# if age>= 18:
#   print("vote") 
# else:
#   print("cant vote")

"""l = [11,22,33,44,55]
print(l)
print(type(l))
"""
"""
l = [11,22,33,44,55]
l.append(90)
print(l)"""
"""
l = [11,22,33,44,55]
l.remove(11)
print(l)
"""
"""l = [11,22,33,44,55]
l.pop(1)
print(l)"""
"""
l = [11,22,33,44,55]
l.sort(reverse=True)
print(l)
"""
"""l = [11,22,33,44,55]
l.sort()
print(l)"""

"""l = [11,22,33,44,55]
l.clear()
print(l)"""
"""
l = [11,22,33,44,55]
l1 = [23,44,55,66,77]
l.extend(l1)
print(l)"""

"""l = [11,22,33,44,55]
print("max = ",max(l))
print("min = ",min(l))
print("sum = ",sum(l))
print("len = ",len(l))"""
"""
l = [11,22,33,44,55]
print(l[::])
print(l[::-1])
print(l[::-2])
print(l[::-3])"""
"""
t = (11,22,33,44)
print(t)
print(type(t))"""

"""t = (11,22,33,44)
print("max = ",max(t))
print("min = ",min(t))
print("sum = ",sum(t))
print("len = ",len(t))"""

"""t = (11,22,33,44)
print(t[::])
print(t[::-1])
print(t[::-2])
print(t[::-3])"""

"""t = ("sudam","galande")
first_name,last_name = t 
print(first_name,last_name)"""

"""s = {11,22,33,44,55}
s.add(90)
print(s)"""

"""s = {11,22,33,44,55}
s.remove(22)
print(s)"""

"""s = {11,22,33,44,55}
s.pop()
print(s)"""

"""s = {11,22,33,44,55}
s1 = {11,22,66,77,88}
print("union = ",s | s1)
print("intersection = ",s & s1)
print("difference = ",s - s1)"""

"""d = {
    "name":"sudam",
    "age":21
}
print(d)
print(type(d))"""

"""d = {
    "name":"sudam",
    "age":21
}
d["name"] = "keshav"
print(d)
"""
"""d = {
    "name":"sudam",
    "age":21
}
d['class'] = "bca ty"
print(d)"""

"""d = {
    "name":"sudam",
    "age":21
}
d.clear()
print(d)"""

"""d = {
    "name":"sudam",
    "age":21
}
print(d.keys())
print(d.values())
print(d.items())"""
"""
a = 10 
b = 20 
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)"""

"""a = [11,22,33,44,55] 
print(11 in a)
print(11 not in a)"""

"""a = 10 
b = 2 
print(a // b)"""

"""a = True 
b = False 
print(a and b )
print(a or b) 
print(not a)"""

"""for i in range(1,10):
    print(i)"""

"""i = 0 
while i <= 10:
    print(i)
    i = i + 1"""
"""
age = int(input("enter age = ")) 
if age >= 19:
    print("vote") 
else:
    print("cant vote")   """ 

"""def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i 
    print("factorial = ",fact) 
fact(5)        
"""
"""s = "sudam"
print(s.upper())
print(s.lower())
print(s.split("d"))
print(s.title())
print(s.replace("s","o"))
"""

"""import copy 
l = [11,22,33,[44,55]] 
shallow_copy = copy.copy(l)
l[3][1] = 90 
print("shallow_copy = ",shallow_copy)
print("original = ",l)
"""
"""
import copy 
l = [11,22,33,[44,55]] 
deep_copy = copy.deepcopy(l)
l[3][1] = 45
print("deep_copy = ",deep_copy)
print("original = ",l)"""

"""with open(r"url","r") as f:
    c = f.read() 
    print(c)"""
"""
with open(r"url","w") as f:
    f.write("data")
"""

# with open(r"url","a") as f:
#     f.write("append mode")

# with open(r"url","x") as f: 
#     f.write("new file")

# with open(r"url","r") as f:
#     for line in f:
#         print(line.strip())

# try: 
#     x = 10/0
# except:
#   print("not possible")

# try:
#     x = 10/0 
# except Exception as e:
#     print(e)
"""
try: 
    x = 10/0 
except:
    print("not possible") 
finally:
    print("always execute")       """

"""def square(a,b):
    if a == 0: 
       raise ValueError("not possible") 
    else:
        return a/b
print(square(1,3))   """ 

"""add = lambda x,y:x+y
print(add(12,34))"""
"""
n1 = int(input("enter first = "))
n2 = int(input("enter second = ")) 
n3 = int(input("enter third = ")) 

def add(fun,n1,n2,m3):
    return fun(n1,n2,n3)
print(add(lambda a,b,c:(a+b+c)/3,n1,n2,n3)) 
    """
"""
def print_msg(*args):
    print(args)
print_msg("sudam","galande")    """

# def print_msg(**kwargs):
#     print(kwargs) 
# print_msg(name = "sudam",age = 21)    

"""def information(fun):
    def process():
        print("welcome")
        fun()
        print("ok")
    return process 
@information 
def name():
    print("sudam")
name() """      

"""class student:
    def information(self,name):
        self.name = "name" 
    def show(self):
        print(f"name = {self.name}") 
c = student()
c.information("sudam")
c.show()            """

"""class student:
    def __init__(self,name):
      self.name = name 
    def information(self):
       print(f"name = {self.name}")
c = student("sudam")
c.information()      """  

"""class student:
    def __init__(self,name):
      self._name = name 
    def information(self):
       print(f"name = {self._name}")
c = student("sudam")
c.information()      """

"""class student:
    def __init__(self,name):
      self.__name = name 
    def information(self):
       print(f"name = {self.__name}")
c = student("sudam")
c.information()   """   

"""class student:
    def __init__(self,name):
      self.name = name 
    def information(self):
       print(f"name = {self.name}")
class student1(student):
   def __init__(self,name,age):
      super().__init__(name)
      self.age = age 
   def show(self):
      print(f"name = ,{self.name},age = {self.age}")
c = student1("sudam",21) 
c.show()     """
"""
class student:
    def __init__(self,name):
      self.name = name 
    def information(self):
       print(f"name = {self.name}")
class student1(student):
   def __init__(self,name,age):
      super().__init__(name)
      self.age = age 
   def show(self):
      print(f"name = ,{self.name},age = {self.age}")
class student3(student1):
  def __init__(self,name,age,standard):
     super().__init__(name,age) 
     self.standard = standard 
  def describe(self):
     print(f"name = {self.name},age = {self.age},standard = {self.standard}")  
c = student3("sudam",21,"bca")
c.describe() """    
"""
class student:
    def __init__(self,name):
      self.name = name 
    def information(self):
       print(f"name = {self.name}")
class student1:
   def __init__(self,age):
      self.age = age 
   def show(self):
      print(f"age = {self.age}")
class student3(student,student1):
  def __init__(self,name,age,standard):
     student.__init__(self,name)
     student1.__init__(self,age)
     self.standard = standard 
  def describe(self):
     print(f"name = {self.name},age = {self.age},standard = {self.standard}")  
c = student3("sudam",21,"bca")
c.describe() """
"""
class cat:
    def speak(self):
        print("mau")
class dog:
    def speak(self):
        print("bho")
animal = [cat(),dog()] 
for animals in animal:
    animals.speak()   """     

"""l = [11,22,33,44,55]
res = list(map(lambda x:x*x,l))
print(res)   """

"""l = [11,22,33,44,55]
res = list(filter(lambda x:x % 2 == 0,l))
print(res)"""

"""from functools import reduce 
def add(x,y):
    return x+y 
l = [11,22,33,44,55]
res = reduce(add,l)
print(res)"""
