#!/usr/bin/env python
# coding: utf-8

# 
# 
# ## Date : 29/09/2022

# 1. Write a lambda expression to get the product of two numbers
# <br>
# Run test for expression(5,6)
# <br>
# Output: 30
# 

# In[136]:


getProduct = lambda val1,val2 :val1 * val2
getProduct(5,6)


# 2. Write a function to get the area of a circle from the radius.
# <br>
# Hint: remember to import the right modul for being able to calculte the area of the circle.
# <br>
# Run test for function(10)
# <br>
# Output: 314.1592653589793

# In[140]:


from math import pi
##radious = 10
def calArea (radious) : 
    area = pi* radious * radious
    print (area)


# In[141]:


calArea(10)


# 3. Build a simple calculator which can: add, subtract, multiply, divide.
# <br>
# Hint: solve by writing a function that takes as argument two numbers and the operation and <br>
# returns the desired output.<br>
# Run test for function(2,5,’d’)<br>
# Output: 0.4

# In[66]:


def myCalulator (val1,val2,userOperator):
    
    #val1 = float(val1)
   # val2 = float(val2)
   # userinput = None
   # userinput = userOperator
    sysOperator = ['a','s','d']
   # while sysOperator  not in  userinput:
  #  print (val1)
#print (val2)
 #   print (userOperator)
    val1 = float(val1)
    val2 = float(val2)
    #while userOperator in sysOperator :
  #  print ({val1})
  #  print ({val2})   
            
    if userOperator in sysOperator :
        print ('Operator is 'userOperator)
        
        if userOperator == 'a':
            total = val1 + val2
            print('Output',total)  
        elif userOperator == 's':
            total = val1 - val2
            print('Output',total)  
        elif userOperator == 'd':
            total = val1 / val2
            print('Output',total) 
    
    else :
        print (f'"Operator not defiend Please choose \n a for adition" \n d for division \n s for substraction')
        
        
    


# In[133]:


myCalulator (2,5,'d')


# 4. Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.
# Run test for r = Rectangle(5,10)
# r.area()
#  Output: 50

# In[95]:


class Rectangle:
    def __init__(self,length,width):
        self.length =length
        self.width = width
    def area (self):
        area = self.length * self.width
        print(area)
        


# In[96]:


r= Rectangle(5,10)


# In[97]:


r.area()


# 5. Define a class named Shape and its subclass Square.
# Shape objects can be consrtucted by name and length has an area function wich return 0
# Square subclass has an init function which take a length and name as argument and has an
# area method and a describe method what prints the name of the Shape.
#  Print the area from Square class.
# Run test for: s = Square('square',5)
# print(s.area())
# print(s.describe())
#  Output: The area is:
# 25
#  This is a: square

# In[103]:


class Shape:
    def __init__(self,name,lenght):
        self.name =name
        self.width = lenght
    def area (self):
        return 0


# In[129]:


class Square(Shape):
    def __init__(self,name,lenght):
        self.__name =name
        self.__lenght = lenght
    def area (self):
        area = self.__lenght * self.__lenght
       # print(area)
        return area
    def describe (self):
        return self.__name


# In[130]:


s=Square('Square',5)


# In[142]:


print ("The area is :",s.area())


# In[145]:


print ("This is a :",s.describe())

