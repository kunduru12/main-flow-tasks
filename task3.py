#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

# reading the database
d1=pd.read_excel("C:\\Users\\ANUSHA\\Desktop\\tips.xlsx")
# print ing the top 10 rows
print(d1.head(10))


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
# reading the database
d1= pd.read_excel("C:\\Users\\ANUSHA\\Desktop\\tips.xlsx")
# Scatter plot with day against
plt.scatter( d1['day'], d1['tip'])
# Adding Tit le to the Plot
plt.title ("Scatter Plot")
# Setting the X and Y labels
plt.xlabel(' Day')
plt.ylabel ('Tip' )
plt.show( )


# In[15]:


import pandas as pd
import matplotlib.pyplot as plt
# reading the database
d1= pd.read_excel("C:\\Users\\ANUSHA\\Desktop\\tips.xlsx")
plt.scatter( d1['day'], d1['tip'],s=d1['total_bill'])
plt.title ("Scatter Plot")
plt.xlabel(' Day')
plt.ylabel ('Tip' )
plt.colorbar()
plt.show( )


# In[17]:


import pandas as pd
import matplotlib.pyplot as plt
d1= pd.read_excel("C:\\Users\\ANUSHA\\Desktop\\tips.xlsx")
plt.plot(d1['tip'])
plt.plot(d1['size'])
plt.title ("Scatter Plot")
plt.xlabel(' Day')
plt.ylabel ('Tip' )
plt.show( )


# In[18]:


import pandas as pd
import matplotlib.pyplot as plt
d1= pd.read_excel("C:\\Users\\ANUSHA\\Desktop\\tips.xlsx")
plt.bar( d1['day'], d1['tip'])
plt.title ("Bar Chart")
# Setting the X and Y labels
plt.xlabel(' Day')
plt.ylabel ('Tip' )
plt.show( )


# In[29]:


import pandas as pd
import matplotlib.pyplot as plt
d1= pd.read_excel("C:\\Users\\ANUSHA\\Desktop\\tips.xlsx")
plt.hist(d1['size'])
plt.hist(d1['tip'])
plt.title ("Histogram Chart")
# Setting the X and Y labels
plt.xlabel('size ')
plt.ylabel ('Tip' )
plt.show( )


# In[ ]:




