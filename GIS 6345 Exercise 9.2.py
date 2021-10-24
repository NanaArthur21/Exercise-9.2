#!/usr/bin/env python
# coding: utf-8

# In[1]:


fin = open('words.txt')


# In[2]:


def has_no_e(word):


# In[3]:


def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
        return True  


# In[4]:


fin = open('words.txt')


# In[5]:


count = 0


# In[6]:


num_of_words = 113809


# In[7]:


for line in fin:
     word = line.strip()
     if has_no_e(word) == True:
        count += 1
        print(word)


# In[8]:


print(count / num_of_words * 100, '%')


# In[9]:


fin = open('words.txt')


# In[10]:


def has_no_e(word):
    for char in word:
        if char in 'Ee':
            return False
    return True  


# In[11]:


count = 0


# In[12]:


for line in fin:
    word = line.strip()
    if has_no_e(word):
        count += 1
        print (word)


# In[13]:


percent = (count / 113809.0) * 100


# In[14]:


print (str(percent)) + "% of the words don't have an 'e'."


# In[ ]:




