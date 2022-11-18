#!/usr/bin/env python
# coding: utf-8

# In[3]:


print(hello
#fix by adding an end parenthesis and quotes#


# In[4]:


print(x)


# In[5]:


x = x


# syntax errors like adding quotes or parenthesis too early, or forgetting one of them at all, mispelling commands, using the wrong syntax for a certain command

# In[6]:


x = “hello”
y = 25.432
y = str(y)
y = int(y)

#cant convert string of a float into an interger, needs to be an interger in the quote


# In[7]:


dict1 = {“one”: 1, 2: “two”, 3: “three”}
print(dict1[“two”])

#1 needs to be before "one"


# In[8]:


x = [1,2,3,4,5]
x.pop()
x.append(3)
x.pop()
x.pop()
for i in range(0, 5):
	print(arr[i])
    
#length won't reach 5


# In[11]:


car_dict = {
  "brand": "Honda",
  "model": "Accord",
  "year": 2017
}

x = car_dict.get("model")

print(x)


# In[16]:


arr = [1,2,3]
for i in range(0, len(arr)):
    if arr[i] == 5:
        print("found")
        
#arr[3] is the error bc index 3 is not in the list


# In[19]:


decimal = 3.5
int(decimal)


# In[20]:


x = 5
y = "yes"
try:
    print(x+y)
except TypeError:
    print("type error detected")
finally:
    print("this will print regardless")


# In[21]:


x = “hello #no second quotation
y = “goodbye”
z = 2
m = 4.3
arr = [1, 2, 3, 4 x, y] #no comma btwn 4 and x, and x doesn't have second quotation mark
dict1 = {x: 1, y: 3, z: “hello”} 
print(dict1[“hello”]) #needs to be the key, not hello
print(x + y + z) #take out z
arr.pop()
arr.append(“what’s up) #no second quote, can't append
for i in range (0, 4):
	print(arr[i])


# In[22]:


x = "hello
try:
    print(x)
except TypeError:
    print("type error detected")
finally:
    print("this will print regardless")


# In[1]:


#post lab ex


# In[1]:


#1) an error is something that cannot be handeled by the programmer whereas an exception can be. An error is a mistake within the gramatical structure of the code.


# In[3]:


#2) 
geek = "Geeks"
num = 4
print(geek + num + geek)
#change 4 to four- must be a str not int
ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
ages['Michael']
#use get() function
import math
math.sqrt(-10)
#use try and except functions


# In[4]:


#3
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

#these blocks are helpful because finally executes the code regardless the error. catch is helpful for if there could be a suspected error and you would like to try to catch it


# In[5]:


#4
li = [1,2,3,4]
li.pop()
li.pop()
li.pop()
li.pop()
li.pop()
li.pop()
#the error is that the pop function is being used from an empty list, there is no use for li.pop() after line 6


# #5
# The error I make most commonly are type errors. I believe this is because my foundation for understanding the different functions isn't as strong because I haven't had as much pratice and I think with more practice these will become less abundant in my code.

# In[7]:


#6
for i in range(0, len(phones)):
phones.append(i)
print(phones[i])
#there should be an indent because line 1 ends with a colon. line 2 should start with an indent


# In[ ]:




