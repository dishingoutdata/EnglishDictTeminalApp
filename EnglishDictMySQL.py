#!/usr/bin/env python
# coding: utf-8

# In[19]:


import mysql.connector

con = mysql.connector.connect(
user = "Enter username here",
password = "Enter password here",
host = "Enter host IP here",
database = "Enter database name here"    
)

word = input("Enter a word: ")
cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(word))
results = cursor.fetchall()

if results:
    
    for result in results:
        print(result)

else:
    print('No word found!')


# In[ ]:





# In[ ]:




