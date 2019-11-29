#!/usr/bin/env python
# coding: utf-8

# In[1]:


import this


# In[2]:


a=9
b=10
print(a)
print(b)

print(id(a))
print(id(b))


# In[3]:


a = 2
print(type(a))
a = '1'
print(type(a))
a = a + '1'   
print(a)
b = int(a) + 8
print(type(b))
print(b)


# In[4]:


a = "Abdul Muiz"
dir(a)


# In[5]:


a = "abdul muiz"
print(a.upper())       
a = a.upper()          
print(a.capitalize())


# In[6]:


a = "Abdul Muiz"
print(len(a))
print(a.strip())
b = len(a.strip())
print(b)
print('We saved ',len(a) - b,' Charecters Space/Memory ')


# In[7]:


c = a.split()  
print(c)
['Abdul', 'Muiz']
d = " ".join(c)      
print(d)


# In[13]:


card = """
    Name    : Abdul Muiz
    Reg     : abc-123
    Program : PIAIC
"""


cards = """
    Name : {name}
    Reg : {reg}
    Program : {program}
"""

print(cards)
    
name = "Abdul Muiz"
reg = "abc-123"
program = "PIAIC"

cards = """
    Name : {}
    Reg : {}
    Program : {}
"""

print(cards.format(name,reg,program))
  


# In[17]:



 name = "Abdul Muiz"
reg = "abc-123"
program = "PIAIC"

print("Name : " + name + "\nReg : " + reg + "\nProgram : " + program)


# In[ ]:





# In[ ]:




