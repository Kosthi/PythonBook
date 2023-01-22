#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Employee:
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, add_salary = 5000):
        self.salary += add_salary


# In[7]:


import unittest

class TestEmployeeCase(unittest.TestCase):
    
    def setUp(self):
        self.employee = Employee('Yimin', 'Wu', 200000)
    
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(205000, self.employee.salary)
        
    def test_give_custom_raise(self):
        self.employee.give_raise(2000)
        self.assertEqual(202000, self.employee.salary)
        
if __name__ == '__main__':
    unittest.main()


# In[8]:


get_ipython().system('jupyter nbconvert --to script 11.2.ipynb')


# In[ ]:




