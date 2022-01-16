#!/usr/bin/env python
# coding: utf-8

# In[5]:


from datetime import datetime
from elasticsearch import Elasticsearch
import matplotlib.pyplot as plt
import pandas as pd
import requests
import time


# In[6]:


es_ip = "http://127.0.0.1:9200"


# In[7]:


es = Elasticsearch(es_ip)


# In[8]:


res = es.get(index="winlogbeat", id="Lc3m130BMs_nTerjc8Ux")a
print(res['_source'])


# In[12]:


query_str = {"size": 0,"aggregations": {"result": {"terms": {"field": "host.name.keyword","order": [{"_count": "desc"}]}}}}
res = es.search(index="winlogbeat", body=query_str)
result = res["aggregations"]["result"]["buckets"]


# In[14]:


host_pd = pd.DataFrame(result, columns=["key", "doc_count"])
#print(host_pd)
host_pd.plot(x="key", y="doc_count", kind="barh");
plt.xlabel('host.name')
plt.ylabel('Log Count')
plt.title('Host Logs')


# In[ ]:




