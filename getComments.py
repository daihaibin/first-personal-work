#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import re
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'}


# In[2]:


def getinfo():
    global cursor,source
    for i in range(0,1269):
        url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + cursor + '&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=' + source
        data = requests.get(url, headers=headers).content.decode()
        
        cursor = re.findall('"last":"(.*?)"',data,re.S)[0] #准备下一页URL的cursor值
        source = str(int(source)+1) #准备下一页URL的source值
        
        comment = re.findall('"content":"(.*?),"',data,re.S) #爬取当前页的评论
        comments.append(comment) #将所有的评论拼接
    return comments


# In[3]:


def writejson(comments):
    with open('comments.json','a',encoding = 'UTF-8') as jsonfile:
        for info in comments:
            for data in info:
                jsonfile.write(data) #写文件
                jsonfile.write('\n') #每条评论中间换行


# In[5]:


comments = []
cursor = '0'
source = '1614090658787'
comments = getinfo()
writejson(comments)

