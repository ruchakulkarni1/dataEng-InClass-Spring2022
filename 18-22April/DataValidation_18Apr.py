#!/usr/bin/env python
# coding: utf-8

# In[79]:


import pandas as pd
from numpy import mean

df = pd.read_csv('./data.csv')


# In[80]:


CrashesDF = df[df['Record Type'] == 1]
VehiclesDF = df[df['Record Type'] == 2]
ParticipantsDF = df[df['Record Type'] == 3]

CrashesDF = CrashesDF.dropna(axis=1,how='all')
VehiclesDF = VehiclesDF.dropna(axis=1,how='all')
ParticipantsDF = ParticipantsDF.dropna(axis=1,how='all')


# In[81]:


#Check if every crash occuurred during year 2019
crash_year = df['Crash Year']

if ((CrashesDF['Crash Year'] == 2019.0).all()):
    print("All crashes occuurred during year 2019")
else:
    print("WARN: Some crashed did not occurr in 2019")


# In[82]:


#Check if every crash occuurred on highway 26
if (CrashesDF['Highway Number'] == 26).all():
    print("All crashes occuurred on highway 26")
else:
    print("WARN: Some crashed did not occurr on highway 26")


# In[5]:


#Every Crash occurred on a date
if(CrashesDF['Crash Year'].isnull().values.any() or
   CrashesDF['Crash Month'].isnull().values.any() or
   CrashesDF['Crash Day'].isnull().values.any()):
    print("WARN: Some crashes does not have a date")
else:
    print("All crashes has a date")


# In[ ]:





# In[83]:


#“Every crash has a unique ID”
if(CrashesDF['Crash ID'].is_unique):
    print("Every crash has a unique ID")
else:
    print("WARN: Every crash does not have a unique ID")


# In[ ]:





# In[39]:


#“Latitude and Longitude must present together”
if(not CrashesDF['Latitude Degrees'].isnull().values.any() and not CrashesDF['Latitude Minutes'].isnull().values.any()
  and not CrashesDF['Latitude Seconds'].isnull().values.any()):
    if(not CrashesDF['Longitude Degrees'].isnull().values.any() and not CrashesDF['Longitude Minutes'].isnull().values.any()
      and not CrashesDF['Longitude Seconds'].isnull().values.any()):
        print("Longitude details are present along with Latitude details for all crashes")
    else:
        print("Latitude details are present but Longitude details are missing for some crashes")
else:
    print("Latitude details are missing for some crashes")


# In[42]:


#Every vehicle listed in the crash data was part of a known crash
#VehiclesDF['Vehicle ID'].isin()
#print(VehiclesDF)


# In[42]:


#“There were thousands of crashes but not millions”
if(len(CrashesDF['Crash ID']) < 1000000):
    print("There are thousands of crashes not millions");
else:
    print("There are millions of crashes");


# In[ ]:





# In[39]:


#“Every vehicle listed in the crash data was part of a known crash”
if(VehiclesDF['Crash ID'].isnull().values.any()):
    print("Some vehicles are not associated with any Crash ID")
else:
    print("Every vehicle listed in the crash data was part of a known crash")


# In[44]:


#“Every participant record is part of crash”
if(ParticipantsDF['Crash ID'].isnull().values.any()):
    print("Some participants are not associated with any Crash ID")
else:
    print("Every participant listed in the crash data was part of a known crash")


# In[77]:


vehDupCrashID = 0
#print(VehiclesDF.duplicated('Crash ID'))

vdf = df.groupby(['Crash ID', 'Vehicle ID']).size().reset_index(name='count')
if((vdf['count'] >= 1).all()):
    print("There is at least one vehicle per crash")
else:
    print("There are few crashes which does not include any vehicle record")
    
pdf = ParticipantsDF.groupby(['Crash ID']).size().reset_index(name='count')
if((pdf['count'] >= 1).all()):
    print("There is at least one participant per crash")
else:
    print("There are few crashes which does not include any participant record")


# In[70]:



if(5 <= mean(CrashesDF['Crash Month']) or mean(CrashesDF['Crash Month']) >= 7 ):
    print("crashes are evenly/uniformly distributed throughout the months of the year")
else:
    print("crashes are not uniformly distributed throughout the months of the year")


# In[78]:


CrashesDF.to_csv(r'C:\Users\rucha\Desktop\Rucha-PSU\Spring2022\DataEngineering\InClass Assignments\18April\Crashes.csv', index=False)
VehiclesDF.to_csv(r'C:\Users\rucha\Desktop\Rucha-PSU\Spring2022\DataEngineering\InClass Assignments\18April\Vehicles.csv', index=False)
ParticipantsDF.to_csv(r'C:\Users\rucha\Desktop\Rucha-PSU\Spring2022\DataEngineering\InClass Assignments\18April\Participants.csv', index=False)


# In[ ]:




