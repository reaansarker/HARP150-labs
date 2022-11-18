#!/usr/bin/env python
# coding: utf-8

# In[1]:


flowers= ['rose', 'calla lily', 'buttercup', "sunflower"]

for flower in flowers:
    print(flower)


# In[2]:


holidays = ["halloween", "thanksgiving", "star wars day", "fourth of july"]
for holiday in holidays:
    print("my favorite holiday is " + holiday)


# In[3]:


superheroes = ["superman", "batman", "spiderman"]
for superhero in superheroes:
    print(superhero)


# In[4]:


superheroes = ["superman", "batman", "spiderman"]
for superhero in superheroes:
    print("now entering the scene...", superhero)
print("which villians will come out to rumble?")


# In[5]:


superheroes = ["superman", "batman", "spiderman"]
for superhero in superheroes:
    print("now entering the scene...")
    print(superhero)
print("which villians will come out to rumble?")


# In[7]:


superheroes = ["superman", "batman", "spiderman"]
for superhero in superheroes:
    print("everyone knows " + superhero + " is the best!")


# In[8]:


print(list(range(15, 25)))


# In[10]:


name = "reaan sarker"
for x in range(1,8):
    print(x,name)


# In[11]:


i = 1
while i < 8:
    print(i)
    i += 1


# In[12]:


glass = 0
glass_capacity = 16

while glass < glass_capacity:
    print(glass)
    glass += 1


# In[ ]:


a = 0
while a < 10:
  print(a)
a += 1


# In[ ]:


from random import randint

roll_loop = True

while(roll_loop):
    print(randint(1, 6))
    if input("Press \"Y\" to roll again. ").upper() != "Y":
        roll_loop = False


# In[ ]:


i = 1
while i < 15:
  print(i)
  if i == 11:
    break
  i += 1

break


# In[ ]:


i = 0
while i < 15:
  i += 1
  if i == 7:
    continue
  print(i)

continue 


# In[ ]:


i = 1
while i < 8:
  print(i)
  i += 1
else:
  print("i is no longer less than 8")


# In[ ]:


current_page = 95
book_len = 100

while current_page <= book_len:
    print("you are on page" + current_page)
    current_page += 1
else:
    print("you finished the book")


# In[ ]:


user_name = input("please enter your name:")
print(user_name)


# In[ ]:


answer = "4"
guess = input("guess what number im thinking of (1-10): ")
while guess guess != answer:
    guess = input("try again: ")
print("yes!")


# In[ ]:


#post lab ex


# In[ ]:


#1) break, continue


# In[ ]:


foods = ["pasta", "sushi", "brownies", "ice cream"]
for food in foods:
    print("my favorite food is " + food + "!")


# In[ ]:


import random

def main():
    nums = []
    for n in range(10):
        number = random.randint(10, 90)
        nums.append(number)


# In[ ]:


import random
i = 0
while i < 5:
    print(random.randint(1, 100000))
    i += 1


# In[ ]:


for n in [1,2,3]:
    square = n**2
    print(n,'squared is',square)
for n in [1,2,3]:
    cube = n**3
    print(n,'cubed is',square)
for n in [1,2,3]:
    fourth = n**4
    print(n,' to the fourth power is',square)


# In[ ]:




