#!/usr/bin/env python
# coding: utf-8

# In[7]:


def show_citys(city, country, population = 0):
    if population:
        return f'{city}, {country} - population {population}'.title()
    else:
        return f'{city}, {country}'.title()


# In[12]:


import unittest

class CitysTestCase(unittest.TestCase):
    def test_city_country(self):
        str = show_citys('Beijing', 'China')
        self.assertEqual(str, 'Beijing, China')
    def test_city_country_population(self):
        self.assertEqual(show_citys('Beijing', 'China', 500000), 'Beijing, China - Population 500000')

if __name__ == '__main__':
    unittest.main()


# In[13]:


get_ipython().system('jupyter nbconvert --to script 11.1.ipynb')


# In[ ]:




