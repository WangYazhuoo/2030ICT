#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[31]:


import numpy as np
x = np.linspace(0, 5, 11)
y = x ** 2


# In[32]:


x


# In[33]:


y


# In[34]:


plt.plot(x, y, 'r')
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')
plt.show()


# In[18]:


plt.subplot(2,2,1)
plt.plot(x, y, 'r--')
plt.subplot(2,2,2)
plt.plot(y, x, 'g*-')
plt.subplot(2,3,4)
plt.plot(y, x, 'g*-')


# In[19]:


fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y, 'b')
axes.set_xlabel('Set x label')
axes.set_ylabel('Set y Label')
axes.set_title('Set Title')


# In[22]:


fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x, y, 'b')
axes1.set_xlabel('X_labell_axes2')
axes1.set_ylabel('Y_labell_axes2')
axes1.set_title('Axes 2 Title')

axes2.plot(y, x, 'r')
axes2.set_ylabel('Y_labell_axes2')
axes2.set_xlabel('X_labell_axes2')
axes2.set_title('Axes 2 Title')


# In[35]:


fig, axes = plt.subplots()
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')


# In[36]:


fig, axes = plt.subplots(nrows=1, ncols=2)


# In[37]:


axes


# In[38]:


for ax in axes:
    ax.plot(x, y, 'b')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
    
fig


# In[42]:


fig, axes = plt.subplots(nrows=1, ncols=3)
for ax in axes:
    ax.plot(x, y, 'g')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
    
fig
plt.tight_layout()


# In[43]:


fig = plt.figure(figsize=(8,4), dpi=100)


# In[ ]:




