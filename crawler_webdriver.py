#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import html5lib
import os #為了建立資料夾
import sys #控制抓取文章頁數 system的縮寫
import numpy as np
import pandas as pd
from selenium import webdriver #動態爬蟲
import csv


# In[2]:


url = 'https://www.cna.com.tw/list/aspt.aspx'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html5lib')
n=0
labels=[]
while n < len(soup.select_one('#pnProductNavContents > ul').findAll('li')):
    try :
        lab = soup.select_one('#pnProductNavContents > ul').findAll('li')[n].find('a',{'class':'first-level'}).text
        url =soup.select_one('#pnProductNavContents > ul').findAll('li')[n].find('a',{'class':'first-level'})['href']
    except:(TypeError,IndentationError)
    labels.append((url,lab))
    n += 1
labels = list(set(labels))
labels.remove(('http://cnavideo.cna.com.tw', '影音'))
labels.remove(('https://www.cna.com.tw/list/sp.aspx', '專題'))
labels.remove(('https://howlife.cna.com.tw/readbook', '悅讀'))
labels.remove(('/list/aall.aspx', '即時'))


# In[3]:


print(labels)


# In[4]:


temp = []
temp.append(('https://www.cna.com.tw/list/ahel.aspx', '生活'))
temp.append(('https://www.cna.com.tw/list/amov.aspx', '娛樂'))
temp.append(('https://www.cna.com.tw/list/acn.aspx', '兩岸'))
temp.append(('https://www.cna.com.tw/list/aipl.aspx', '政治'))
temp.append(('https://www.cna.com.tw/list/asoc.aspx', '社會'))
temp.append(('https://www.cna.com.tw/list/aloc.aspx', '地方'))
temp.append(('https://www.cna.com.tw/list/ait.aspx', '科技'))
temp.append(('https://www.cna.com.tw/list/acul.aspx', '文化'))
temp.append(('https://www.cna.com.tw/list/aopl.aspx', '國際'))
temp.append(('https://www.cna.com.tw/list/asc.aspx', '證券'))
temp.append(('https://www.cna.com.tw/list/aie.aspx', '產經'))
temp.append(('https://www.cna.com.tw/list/aspt.aspx', '運動'))
temp[1][1]


# In[5]:


driver = webdriver.Chrome()
driver.get(temp[11][0])

driver.find_element_by_link_text(u"看更多內容").click()
driver.find_element_by_link_text(u"看更多內容").click()
driver.find_element_by_link_text(u"看更多內容").click()
driver.find_element_by_link_text(u"看更多內容").click()

soup = BeautifulSoup(driver.page_source,'html.parser')
driver.close()
print(soup)


# In[6]:


new_url = []

for i in range(100):
    lab_url = soup.findAll('div',{'class':'statement'})[0].findAll('ul',{'class':'mainList imgModule'})[0].findAll('li')[i].find_all('a')[0]['href']
    new_url.append(lab_url)
    new_url.append(temp[11][1])

new_url = np.array(new_url).reshape(100,2)
new_url = pd.DataFrame(new_url)
new_url.head()


# In[7]:


news=[]
for i in range(100):
    res = requests.get(new_url[0][i])
    soup = BeautifulSoup(res.text,'html5lib')
    txt = ""
    try:
        for s in soup.find_all('div',{'class':'paragraph'})[0].findAll('p'):
            txt=txt+s.getText()
    except:IndexError
    news.append(txt)
    news.append(new_url[1][i])


# In[8]:


news


# In[9]:


news = np.array(news).reshape(100,2)
news = pd.DataFrame(news)


# In[10]:


news.columns = ['新聞','類別']
news.head()


# In[11]:


news.to_csv('D:\\jupyter\\news_class_output\\sport.csv', encoding="cp950")


# In[ ]:


# with open(u"news_class_output.csv",'a+') as f:
#     csv_write = csv.writer(f)
    
#     for i in range(100):
#         data_row = [news['新聞'][i],news['類別'][i]]
#         csv_write.writerow(data_row)


# In[ ]:





# In[ ]:





# In[ ]:




