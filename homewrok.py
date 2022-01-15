#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
from elasticsearch import Elasticsearch
import matplotlib.pyplot as plt
import pandas as pd
import requests
import time


# In[2]:


es_ip = "http://127.0.0.1:9200/"


# In[3]:


es = Elasticsearch(es_ip)


# In[4]:


res = es.get(index="winlogbeat", id="A83i130BMs_nTerjzcUN")
print(res['_source'])


# In[5]:


query_str = {"size": 0,"aggregations": {"result": {"terms": {"field": "winlog.computer_name.keyword","order": [{"_count": "desc"}]}}}}
res = es.search(index="winlogbeat", body=query_str)
result = res["aggregations"]["result"]["buckets"]


# In[7]:


computer_pd = pd.DataFrame(result, columns=["key", "doc_count"])
#print(event_pd)
computer_pd.plot(x="key", y="doc_count", kind="bar");
plt.xlabel('Computer ID')
plt.ylabel('Log Count')
plt.title('computer')







