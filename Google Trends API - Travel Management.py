#!/usr/bin/env python
# coding: utf-8

# # Travel Mangement Key Word soearch on google Trends using Google Trends API
# 
# # It enables marketers target specific region that have the highets keyword search fro travel manegment and offer solutions
# 

# In[14]:


from pytrends.request import TrendReq

# Define your keywords in a list
keywords = ['Travel Management']

# Create a dictionary with 'kw_list' as key and your keywords list as value
kw_list = {'kw_list': keywords}

# Initialize pytrends and build payload using the defined kw_list and specify the country as Kenya
pytrend = TrendReq(hl='en-KE')  # 'hl' parameter sets the language to English and 'geo' parameter sets the region to Kenya

# Build payload with the defined kw_list and the geo parameter for Kenya
pytrend.build_payload(kw_list['kw_list'], geo='US')

# Fetch interest by region for Kenya
Travel_df = pytrend.interest_by_region()

# Display the top 10 rows
Travel_df.head(10)



# In[13]:


import matplotlib.pyplot as plt

# Sort the DataFrame in descending order based on the 'Travel Management' column
sorted_df = Travel_df.sort_values(by='Travel Management', ascending=False)

# Select the top ten rows
top_ten = sorted_df.head(10)

# Display the top ten regions
print("Top Ten Regions with Highest Interest in Travel Management:")
print(top_ten)

# Create a pie chart using the 'top_ten' DataFrame
plt.figure(figsize=(8, 6))  # Adjust the figure size if needed
top_ten['Travel Management'].plot(kind='pie', autopct='%1.1f%%', startangle=140)

# Add title and labels
plt.title('Top Ten Regions with Highest Interest in Travel Management in USA')
plt.ylabel('')  # No need for y-label, as it's redundant in a pie chart

# Display the pie chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()


# In[ ]:




