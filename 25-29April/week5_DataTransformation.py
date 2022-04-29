#!/usr/bin/env python
# coding: utf-8

# In[79]:


import pandas as pd
from numpy import mean
import numpy as np

booksDF = pd.read_csv('./books.csv')
#print(booksDF)


# In[107]:


newBooksDF=booksDF.drop(columns=['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 'Issuance type', 'Shelfmarks'])

print(newBooksDF)


# In[80]:


df = pd.read_csv('./books.csv', usecols=["Identifier", "Place of Publication", "Date of Publication", "Publisher", "Title", "Author", "Contributors", "Flickr URL"])
print(df)


# In[47]:


df['Date of Publication'] = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
print(df)


# In[48]:


df['Date of Publication'].dtype


# In[49]:


df['Date of Publication'] = pd.to_numeric(df['Date of Publication'])
df['Date of Publication'].dtype


# In[84]:


df['Place of Publication']=df['Place of Publication'].str.extract(r'([^\s]+)').replace(r'[^\w\s]+', '',regex=True)
print(df)


# In[100]:


import re
uniplaces = []
with open('./uniplaces.txt') as file:
    for line in file:
        if '[edit]' in line:
            state = line
        else:
            #print(re.findall(r'\(.*?\)', line)[0])
            city=line.split(' ')[0]
            university=re.findall(r'\(.*?\)', line)
            uniplaces.append((state, city, university))
print(uniplaces)


# In[101]:


uniDF = pd.DataFrame(uniplaces, columns=['State', 'City', 'University'])
print(uniDF)


# In[103]:


import re
def getCleanedData(item):
    #print(item)
    if ' (' in item:
        return item[:item.find(' (')]
    elif '[' in item:
        return item[:item.find('[')]
    else:
        return item
uniDF =  uniDF.applymap(getCleanedData)
print(uniDF)


# In[57]:


trimetDF = pd.read_csv('trimet.csv')

print(trimetDF) 


# In[ ]:





# In[58]:


tempDF = []
for idx, row in trimetDF.iterrows():
    num = row['OCCURRENCES']
    for i in range(num):
        tempDF.append(row)

trimetDF = trimetDF.append(tempDF)
print(trimetDF);


# In[59]:


trimetDF['VALID_FLAG'].isnull().values.any()


# In[63]:


#trimetDF['VALID_FLAG']=trimetDF['VALID_FLAG'].ffill()
trimetDF['VALID_FLAG']=trimetDF['VALID_FLAG'].interpolate(method='linear')


# In[66]:


trimetDF['VALID_FLAG'].isnull().values.any()


# In[94]:


trimetDF['ARRIVE_TIME'].isnull().values.any()


# In[97]:


trimetDF['ARRIVE_TIME']=trimetDF['ARRIVE_TIME'].interpolate(method='linear')


# In[98]:


trimetDF['ARRIVE_TIME'].isnull().values.any()


# In[18]:


#Section G
df = pd.DataFrame({"names": ['Jane', 'John', 'Ashley', 'Max', 'Emily'], "A":[1,8,6,0,7], "B":[6,1,3,3,6], "C":[6,2,5,4,6], "D":[9,8,1,0,0],
                  "E":[1,8,7,8,6]})
df


# In[19]:


#Add / drop columns
#The first and foremost way of transformation is adding or dropping columns. A new column can be added as follows:
df['new'] = np.random.random(5)
df


# In[20]:


df.drop('new', axis=1, inplace=True)
df


# In[21]:


#Add / drop rows
#We can use the loc method to add a single row to a dataframe.
df.loc[5,:] = ['Jack', 3, 3, 4, 5, 1]
df


# In[22]:


df.drop(5, axis=0, inplace=True)
df


# In[23]:


#insert
df.insert(0, 'new', np.random.random(5))
df


# In[24]:


#melt
meltdf=pd.DataFrame({"names": ['Jane', 'John', 'Jack'], "day1":[1,5,4], "day2":[5,1,9], "day3":[8,3,8], "day4":[5,2,6],
                  "day5":[3,8,3]})
meltdf


# In[25]:


pd.melt(meltdf, id_vars='names').head()


# In[27]:


#concat
df1=pd.DataFrame({"names": ['Jane', 'John', 'Jack'], "day1":[1,5,4], "day2":[5,1,9], "day3":[8,3,8], "day4":[5,2,6],
                  "day5":[3,8,3]})
df2=pd.DataFrame({"names": ['Max', 'Emily', 'Ashley'], "day1":[9,6,0], "day2":[0,8,2], "day3":[7,1,2], "day4":[4,9,4],
                  "day5":[5,0,0]})
print(df1)
print(df2)


# In[29]:


pd.concat([df1, df2], axis=0, ignore_index=True)


# In[32]:


#Merge
customer=pd.DataFrame({"id":[1,2,3,4,5], "name": ['Jane', 'John', 'Jack', "Ashley", "Emily"], "ctg":['A', 'A', 'C', 'B', 'B']})
order=pd.DataFrame({"id":[2,4,5,6], "amount": [24,32,25,44], "payment":["Credit card", "Credit card", "cash", "cash"]})
print(customer)
print(order)


# In[33]:


customer.merge(order, on='id')


# In[35]:


#Get Dummies
dummydf=pd.DataFrame({"name": ['Jane', 'John', 'Jack', "Ashley", "Emily"], "ctg":['A', 'A', 'C', 'B', 'B'], "vals":[14.2, 21.4, 15.6, 12.1, 17.7]})
dummydf


# In[37]:


pd.get_dummies(dummydf)


# In[38]:


pivotdf=pd.DataFrame({"name": ['Jane', 'John', 'John', 'John', 'Jane', 'Jane', 'Jane', 'John'], "ctg":['A', 'A', 'C', 'B', 'B', 'C', 'C', 'B'], "vals":[14.2, 21.4, 15.6, 12.1, 17.7, 12.5, 8.6, 19.1]})
pivotdf


# In[39]:


pivotdf.pivot_table(index='name', columns='ctg', aggfunc='mean')


# In[43]:


#Section G Part 2

gdf = pd.read_excel('Data_Extract_From_World_Development_Indicators.xlsx')
print(gdf.head())


# In[44]:


meltgdf = pd.melt(gdf, 'Country Name', var_name='Date', value_name='GDPperCapGrowth%')
print(meltgdf.head())


# In[45]:


meltgdf.to_excel(r'output.xlsx', sheet_name='GDPperCapGr', index=False)


# In[ ]:




