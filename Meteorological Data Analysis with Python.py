#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv('D:\documents\weatherHistory.csv' , parse_dates = ['Formatted Date'] , index_col = ['Formatted Date'])


# In[3]:


data.head()


# In[4]:


data.info()


# In[5]:


data.isnull().sum() # there are 517 null columns


# In[6]:


new_data = data.dropna() # remove null columns and store it in a new data set


# In[7]:


new_data.info()


# In[8]:


new_data.describe()


# In[9]:


new_data.index = pd.to_datetime(new_data.index , utc =True)


# In[11]:


resampled_data = new_data.resample('M').mean() # resample accroading to Month end ('M')


# In[12]:


resampled_data.head()


# In[13]:


resampled_data.tail()


# In[14]:


resampled_data['month'] = resampled_data.index.month


# In[15]:


resampled_data['year'] = resampled_data.index.year


# In[16]:


resampled_data.head()


# In[17]:


resampled_data.index = resampled_data.index.date


# In[18]:


resampled_data = resampled_data[1:] # remove column with year 2005 column


# In[19]:


resampled_data.head()


# In[20]:


month_to_month_AT = {}
for month in range(1,13):
    month_to_month_AT[month] = list(resampled_data[resampled_data['month'] == month]['Apparent Temperature (C)'].values)


# In[21]:


title = {1:'Jan',2:'Feb',3:'March',4:'April',5:'May',6:'June',7:'July',8:'Aug',9:'Sep',
         10:'Oct',11:'Nov',12:'Dec'}
def plot_AT_or_Humidity(what_for , month_dict):
    for index in range(1,13):
        t = title[index]
        plt.plot(range(2006,2017),month_dict[index])
        plt.title(what_for + ' for ' +t+' Month')
        plt.show()


# In[22]:


month_to_month_Humidity = {}
for month in range(1,13):
    month_to_month_Humidity[month] = list(resampled_data[resampled_data['month'] == month]['Humidity'].values)


# In[23]:


def find_avg_difference(month_dict):
    difference = []
    for month in range(1,13):
        difference.append(np.mean(month_dict[month]))
    return difference


# In[24]:


AT_difference_monthly = find_avg_difference(month_to_month_AT)
Humidity_difference_monthly = find_avg_difference(month_to_month_Humidity)


# In[25]:


plt.plot(AT_difference_monthly)
plt.title('Monthly Average Data(2006-2016) of AT')


# In[26]:


plt.plot(Humidity_difference_monthly)


# In[27]:


new_data.index = new_data.index.date


# In[28]:


new_data.index = pd.DatetimeIndex(new_data.index)


# In[29]:


pd.options.mode.chained_assignment = None


# In[30]:


new_data['month'] = new_data.index.month
new_data['year'] = new_data.index.year


# In[31]:


def find_average_monthly_AT_or_Humidity(what_for):
    avg_data_tempreature_monthly = {}
    for year in range(2006,2017):
        for month in range(1,13):
            result = list(new_data.loc[(new_data['month'] == month)&(new_data['year']==year) , :][what_for].values)
            if month not in avg_data_tempreature_monthly:
                avg_data_tempreature_monthly[month] = [np.mean(result)]
            else:
                avg_data_tempreature_monthly[month].append(np.mean(result))
    return avg_data_tempreature_monthly


# In[32]:


AT_monthly_average = find_average_monthly_AT_or_Humidity('Apparent Temperature (C)')
Humidity_monthly_average = find_average_monthly_AT_or_Humidity('Humidity')


# In[33]:


AT = pd.DataFrame(AT_monthly_average)
AT['year'] = range(2006,2017)


# In[34]:


H = pd.DataFrame(Humidity_monthly_average)
H['year'] = range(2006,2017)


# In[35]:


for month in range(1,13):
    sns.barplot(x = AT['year'] , y = AT[month])
    
    plt.title('Bar plot for Month :' + title[month])
    plt.show()


# In[36]:


for month in range(1,13):
    sns.barplot(x = H['year'] , y = H[month])
    
    plt.title('Bar plot for Month :' + title[month])
    plt.show()


# In[37]:


def plot_Humidty_and_AT():
    for month in range(1,12):
        plt.plot(range(2006,2017),AT_monthly_average[month] , label = 'AT' , color = 'red')
        plt.plot(range(2006,2017),Humidity_monthly_average[month] , label = 'Humidity')
        plt.legend()
        plt.title('AT and Humidity (Without Normalization) for Month : '+ title[month])
        plt.show()


# In[38]:


plot_Humidty_and_AT()


# In[39]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[40]:


sns.barplot(H['year'] , H[4])
plt.title('Humidity For April Month')
plt.show()


# In[44]:


sns.barplot(AT['year'] , AT[4])
plt.title('Apparent Temperature For April Month')
plt.show()


# In[46]:


plt.plot(range(2006,2017),AT_monthly_average[4] , label = 'Apparent Temperature(C)' , color = 'red')
plt.plot(range(2006,2017),Humidity_monthly_average[4] , label = 'Humidity')
plt.legend()
plt.title('Apparent Temperature vs Humidity for April Month')
plt.show()


# In[47]:


sns.barplot(H['year'] , H[6])
plt.title('Humidity For June Month')
plt.show()


# In[48]:


sns.barplot(AT['year'] , AT[6])
plt.title('Apparent Temperature For June Month')
plt.show()


# In[49]:


plt.plot(range(2006,2017),AT_monthly_average[6] , label = 'Apparent Tempreature(C)' , color = 'red')
plt.plot(range(2006,2017),Humidity_monthly_average[6] , label = 'Humidity')
plt.legend()
plt.title('Apparent Temperature vs Humidity for June Month')
plt.show()


# In[ ]:


print("Completed by Sandeep Potdukhe")

