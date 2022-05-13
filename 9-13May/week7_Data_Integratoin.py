#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[116]:


censusdf = pd.read_csv('./acs2017_census_tract_data.csv')
censusdf


# In[ ]:





# In[117]:


County_info = censusdf


#create coulm with county name and state
County_info['County'] = County_info['County'] + ", "+County_info['State']

#drop unwanted column state
County_info.drop(columns = ['State'], inplace=True)
County_info


# In[208]:


#County_info.groupby(['County']).sum()
ci['County']=County_info.groupby('County')
ci=County_info.groupby('County').agg({'TotalPop':'sum', 'IncomePerCap':'sum', 'Poverty':'sum'})


# In[239]:


ci['%Poverty'] = (ci['Poverty'] / 
                  ci['TotalPop']) * 100
ci


# In[97]:





# In[238]:


ci


# In[240]:


ci['Id'] = range(1, len(ci) + 1)
ci


# In[133]:


ci.to_excel(r'County_info.xlsx')


# In[215]:



coviddf = pd.read_csv('./COVID_County_data.csv')
coviddf


# In[216]:


Covid_info = coviddf

Covid_info['county'] = Covid_info['county'] + " County"

#create coulm with county name and state
Covid_info['county'] = Covid_info['county'] + ", "+Covid_info['state']

#drop unwanted column state
Covid_info.drop(columns = ['state'], inplace=True)
Covid_info


# In[217]:


Covid_info['date'] = pd.to_datetime(Covid_info['date'])

Covid_info['month']= Covid_info['date'].dt.month_name()
#Covid_info['month']= Covid_info['date'].dt.month
Covid_info['year']= Covid_info['date'].dt.year
Covid_info


# In[218]:


#create coulm with county name and state
#Covid_info['month'] = str(Covid_info['month']) + ", " + str(Covid_info['year'])
Covid_info["Date"] = Covid_info["month"].astype(str) + " " + Covid_info["year"].astype(str)

#drop unwanted column state
#Covid_info.drop(columns = ['year'], inplace=True)
Covid_info


# In[222]:


#covidInfo=Covid_info
#Covid_info['county']=Covid_info.groupby('county')
Covid_info=Covid_info.groupby(['county','Date']).agg({'cases':'sum', 'deaths':'sum'})
Covidinfo=Covid_info


# In[242]:


Covidinfo=Covidinfo.groupby('county').agg({'cases':'sum', 'deaths':'sum'})
Covidinfo['TotalCases']=Covidinfo['cases']
Covidinfo['TotalDeaths']=Covidinfo['deaths']
Covidinfo


# In[243]:


Covidinfo['TotalCasesper100k'] = (Covidinfo['TotalCases'] / 100000)
Covidinfo['TotalDeathsper100k'] = (Covidinfo['TotalDeaths'] / 100000)
Covidinfo


# In[244]:


ci


# In[293]:


cc=ci.join(Covidinfo)
cc


# In[ ]:





# In[310]:


cc.to_excel(r'Covid_summary.xlsx')


# In[272]:


R = cc['TotalCasesper100k'].corr(cc['%Poverty'])
R
ax1 = cc.plot.scatter(x='TotalCasesper100k',
                      y='%Poverty',
                      c='DarkBlue')


# In[273]:


Rd = cc['TotalDeathsper100k'].corr(cc['%Poverty'])
Rd
ax2 = cc.plot.scatter(x='TotalDeathsper100k',
                      y='%Poverty',
                      c='Red')


# In[274]:


R3 = cc['TotalCasesper100k'].corr(cc['IncomePerCap'])
print(R3)
ax3 = cc.plot.scatter(x='TotalCasesper100k',
                      y='IncomePerCap',
                      c='Yellow')


# In[275]:


R4 = cc['TotalDeathsper100k'].corr(cc['IncomePerCap'])
print(R4)
ax4 = cc.plot.scatter(x='TotalDeathsper100k',
                      y='IncomePerCap',
                      c='Red')


# In[316]:


R5 = cc['TotalPop'].corr(cc['TotalCases'])
print(R5)
ax5 = cc.plot.scatter(x='TotalPop',
                      y='TotalCases',
                      c='Yellow')


# In[317]:


R51 = cc['IncomePerCap'].corr(cc['TotalCases'])
print(R51)
ax51 = cc.plot.scatter(x='IncomePerCap',
                      y='TotalCases',
                      c='Yellow')


# In[ ]:





# In[301]:


print(Covidinfo.columns.tolist())


# In[ ]:





# In[303]:


cc3=pd.read_csv('./Covid_summary.csv')
cc3


# In[306]:


orr=cc3[cc3['County'].str.contains("Oregon")]
orr


# In[308]:


Ro1 = orr['TotalCasesper100k'].corr(orr['%Poverty'])
print(Ro1)
axor1 = orr.plot.scatter(x='TotalCasesper100k',
                      y='%Poverty',
                      c='DarkBlue')


# In[309]:


Ro2 = orr['TotalDeathsper100k'].corr(orr['%Poverty'])
print(Ro2)
axor2 = orr.plot.scatter(x='TotalDeathsper100k',
                      y='%Poverty',
                      c='Red')


# In[311]:


Ro3 = orr['TotalCasesper100k'].corr(orr['IncomePerCap'])
print(Ro3)
axor3 = orr.plot.scatter(x='TotalCasesper100k',
                      y='IncomePerCap',
                      c='Yellow')


# In[312]:


Ro3 = orr['TotalDeathsper100k'].corr(orr['IncomePerCap'])
print(Ro3)
axor3 = orr.plot.scatter(x='TotalDeathsper100k',
                      y='IncomePerCap',
                      c='Orange')


# In[315]:


Ro5 = orr['%Poverty'].corr(orr['TotalCases'])
print(Ro5)
axor5 = orr.plot.scatter(x='%Poverty',
                      y='TotalCases',
                      c='Green')


# In[318]:


Ro6 = orr['IncomePerCap'].corr(orr['TotalDeaths'])
print(Ro6)
axor6 = orr.plot.scatter(x='IncomePerCap',
                      y='TotalDeaths',
                      c='Orange')


# In[319]:


Ro7 = orr['TotalPop'].corr(orr['TotalDeaths'])
print(Ro7)
axor7 = orr.plot.scatter(x='TotalPop',
                      y='TotalDeaths',
                      c='Brown')


# In[ ]:




