#!/usr/bin/env python
# coding: utf-8

# In[19]:


name=str(input("İsminiz: "))
surname=str(input("Soyisminiz: "))
age=int(input("Yaşınız: "))
birth=int(input("Doğum yılınız: "))
person=[name,surname,age,birth]


# In[20]:


for i in person:
    
    print(i)


# In[23]:


if 0< age <18:
    print("You can't go out because it's too dangerous")
elif age>18:
        print("You can go out to the street")
else:
     print("Invalid")
        
    
    


# In[ ]:




