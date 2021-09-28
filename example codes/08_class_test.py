#!/usr/bin/env python
# coding: utf-8

# # Classes in Python

#  **Jupyter Notebook** and **Jupyter-Lab**
# 
# - Ctrl + Enter  -->  Run current cell
# - Shift + Enter -->  Run + Go to next cell
# - Alt + Enter   -->  Run + Create new cell

# ## Person Class

# In[9]:


class Person:
    def __init__(self, p_name, p_age):
        self.name = p_name
        self.age = p_age
    
    def show_info(self):
        print(f'''
            name: {self.name}
            age: {self.age}''')


# In[16]:


class Student(Person):
    def __init__(self, s_name, s_age, std_num):
        super().__init__(s_name, s_age)
        self.std_num = std_num
    
    def show_info_std(self):
        print(f'''
            name: {self.name}
            std number: {self.std_num}''')


# In[11]:


p1 = Person('Ali', 32)
p1.show_info()


# In[17]:


s1 = Student('James', 25, 1234567)
s1.show_info()
s1.show_info_std()

