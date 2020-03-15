# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:55:48 2019

@author: ielshal
"""
import os
import shutil
import pandas as pd

# In[1]:

AccountsPath = "C:\\scripts\\vendor_accounts.txt"
Text_File = open(AccountsPath, "r") 
Data = Text_File.read

# In[2]:

Accounts = []
for Name in Text_File:
    Accounts.append(Name.strip())
  
# In[3]:
    
AllState = pd.read_fwf("C:\\scripts\\login_history.txt")
NonActive = AllState[AllState["STATE"] == "Disc"]
NonActive =list(NonActive["USERNAME"])  

# In[4]:

Final_List = [x for x in Accounts if x in NonActive]
        
# In[5]:

Paths = []
for acc in Final_List:
    Paths.append("C:\\Users\\"+acc+"\\AppData\\LocalLow\\Sun\\Java\\Deployment\\cache\\6.0")

# In[6]:

def Get_Existance(path):
    try:
        pth = os.listdir(path)
        return(path)
    except:
        print(pth,"Path Not Exist")
        return(0)
        
# In[7]:
        
Exist = []
for pth in Paths:
    Exist = Get_Existance(pth)
    
Exist = [i for i in Exist if i != 0]
        
# In[5]:
       
filelist = []
    
for pth in Exist:
    for f in os.listdir(pth):
        filelist.append(f)

    for i in filelist:
        try: 
            shutil.rmtree(os.path.join(pth,i))
        except:
            os.remove(os.path.join(pth,str(i)))