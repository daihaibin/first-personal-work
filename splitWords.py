#!/usr/bin/env python
# coding: utf-8

# In[1]:


import jieba

jsonfile = open("comments.json", "r", encoding='UTF-8').read()
words = jieba.lcut(jsonfile, cut_all=False)

stopWords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]
counts = {} 
for word in words:                                # 遍历所有分词，统计每个分词出现的次数
    if len(word) == 1 or word in stopWords:      # 不符合两个条件的其中一项分词直接跳过
        continue
    else:                                         # 词语每出现一次其对应的值加1
        counts[word] = counts.get(word, 0) + 1    # 若字典中不存在word元素，生成元素则并使其对应的数字为0
finalWords = list(counts.items())                      # 把字典每对key和value组成一个元组并把元组放在列表中返回
finalWords.sort(key=lambda x: x[1], reverse=True)     # 根据词语出现的次数进行从大到小排序

finalData = []                                    #为了制作词云图，需要有name和value属性值
for i in range(len(finalWords)):
        Dict = {}
        word, count = finalWords[i]
        if count >= 30:                           #出现频率小于30的省略
            Dict["name"] = word
            Dict["value"] = count
            finalData.append(Dict)
print(finalData)


# In[2]:


import json
with open('countWords.json','a+',encoding='UTF-8') as file:
    json.dump(finalData, file, ensure_ascii=False, indent=4)


# In[ ]:




