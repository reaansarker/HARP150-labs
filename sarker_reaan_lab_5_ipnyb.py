#!/usr/bin/env python
# coding: utf-8

# In[5]:


issue = "tired"

issue == "headache"
if issue == "headache":
    print("Take an advil.")
elif issue == "stomach ache":
    print("Take pepto")
elif issue == "tired":
    print("take a nap.")
elif issue == "backache":
    print("do some stretches")
else:
    print("go to the doctor!")


# In[6]:


weather = "rainy"

if weather == "sunny":
    print("Wear sunglasses")
elif weather == "rainy":
    print("Bring an umbrella")
elif weather == "cold":
    print("Wear a sweater")
elif weather == "hot":
    print("Wear shorts")
else:
    print("Check the weather channel")


# In[7]:


show = "New Girl"

if show == "New Girl":
    print("so good")
elif show == "Glee":
    print("Not that good but addicted")
elif show == "Grey's Anatomy":
    print("so many seasons!!")
elif show == "Bones":
    print("Made me think I liked bio")
else:
    print("Can't wait to watch!")


# In[1]:


7 == 7


# In[2]:


4 == 7


# In[3]:


4 == 4.0


# In[7]:


"dede" == "dede"


# In[6]:


"Dede" == "dede"


# In[8]:


"Dede".lower() == "dede".lower()


# In[9]:


"7" == 7


# In[10]:


4 != 7


# In[11]:


4 != 4


# In[12]:


"7" != 7


# In[13]:


"Tommy" != "tommy"


# In[14]:


"Bologna" != "Bologna"


# In[15]:


5 > 3
5 >= 3
3 >= 3
3 < 5
3 <= 5
3 <= 3
10 > 5
10 >= 5
10 >= 10


# In[16]:


months = ["january", "february", "march", "april"]
print("january" in months)
print("october" in months)


# In[17]:


pies = ["cherry", "pumpkin", "blueberry", "chocolate", "pizza"]
if len(pies) < 2:
    print ("You don’t have many pies")


# In[19]:


if len(pies) > 4:
    print("You must really love pie! You have so many!")


# In[22]:


family = ["Bob", "Linda", "Tina", "Gene", "Louise"]

if len(family) >= 5:
    print("A large family.")
elif len(family) == 4:
    print("An average size family.")
else:
    print("A small family")


# In[23]:


names = ['bonnie', 'clyde']

if 'bonnie' in names:
    print("Hello, Bonnie!")
if 'sam' in names:
    print("Hello, Sam!")
if 'clyde' in names:
    print("Hello, Clyde!")
if 'monty' in names:
    print("Hello, Monty!")


# In[28]:


age = 16
if age == 16 or age == 17 or age == 18:
    print("You are old enough to ride the ferris wheel")
else:
    print("Come back when you are older")

age = 15
if age >= 13 and age <= 19:
    print("You are a teenager")
else:
    print("You are either a baby or an adult.")


# In[30]:


a = 5
b = 10
sum_ab = a + b
product_ab = a * b

if sum_ab > 100:
    print("the sum is", + sum_ab)
else:
    print("the product is", + product_ab)


# In[31]:


a = 15
b = 20
sum_ab = a + b
product_ab = a * b

if sum_ab > 100:
    print("the sum is", + sum_ab)
else:
    print("the product is", + product_ab)


# In[32]:


wallet_money = 20
shirt_min = 10
shirt_price = 15

if shirt_price >= shirt_min and shirt_price <= wallet_money:
    print("I can afford this")
else:
    print("I can't buy it")


# In[33]:


names = ["hellen", "lauren", "chris", "john"]
if len(names) > 3:
    print("they all made it")


# In[34]:


names.pop()
names.pop()
if len(names) > 3:
    print("they all made it")


# In[35]:


names.append("hellen")
names.append("chris")
if "hellen" in names:
    print("true hellen is here")
if "kate" in names:
    print("true kate is here")


# In[36]:


#post lab ex


# In[37]:


food = "pasta"

if food == "pasta":
    print("if you like pasta, move to italy")
elif food == "sushi":
    print("if you like sushi, move to japan")
elif food == "pizza":
    print("if you like pizza, move to new york")
elif food == "chicken tenders":
    print("if you like chicken tenders, move to the south")
else:
    print("stay where you are, enjoy what's there!")


# In[ ]:


number = input("number: ")
numberx = float(number)
if numberx > 0:
    print("positive")
if numberx < 0:
    print("negative")
else:
    print("the number is equal to zero")


# In[ ]:


wallet_money = 50
items = ["shirt", "shoes", "jeans"]
shirt_cost = 7
shoes_cost = 20
jeans_cost = 30

if shirt_cost <= wallet_money:
    print("I have enough for this, and have $" wallet_money - shirt_cost "left!")
else:
    print("This is too much for what I have.")
elif shoes_cost <= wallet_money:
    print("I have enough for this, and have $" wallet_money - shoes_cost "left!")
else:
    print("This is too much for what I have.")
elif jeans_cost <= wallet_money:
    print("I have enough for this, and have $" wallet_money - jeans_cost "left!")
else:
    print("This is too much for what I have.")

if shirt_cost and shoes_cost and jeans_cost <= wallet_money:
    print("I can afford everything I want!")
else:
    print("I can't afford all of this and need to put something back")


# In[ ]:


list = ["Tyler", "tyler", "laura", "Laura", "tina", "Tina"]
correctList = []
for name in list:
    if name.title() == name:
        correctList.append(name)
print(correctList)


# In[ ]:




