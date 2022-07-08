#!/usr/bin/env python
# coding: utf-8

# In[3]:


##ASSIGNMENT 1


# In[13]:


print('*')
print("'hello'")
print(-87.8)
print("-")
print("/")
print("   +")
print(6)


# In[7]:


##In above *,'hello',-87.8,   +,6 are values and expressions are *,-,/


# In[8]:


##string and variables
  ## string is the value representing text and A variable is something that holds a value that may change.


# In[14]:


3. Describe three different data types.
1.Python numeric data -Holds numeric value 
int – holds signed integers of non-limited length.
long- holds long integers(exists in Python 2.x, deprecated in Python 3.x).
float- holds floating precision numbers and it’s accurate up to 15 decimal places.
complex- holds complex numbers.

2. Python String Data Type-The string is a sequence of characters. Python supports Unicode characters.
3.Python Tuple-The tuple is another data type which is a sequence of data similar to a list. But it is immutable. That means data in a tuple is write-protected. Data in a tuple is written using parenthesis and commas.


# In[ ]:


get_ipython().set_next_input('4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')
Expression is made up of values, containers, and mathematical operators and they are used to evaluate the values 
or represent the result on the screen.
For example :Sum=3+7


# In[ ]:


get_ipython().set_next_input('5. This assignment statements, like spam = 10. What is the difference between an expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')

Expression is made up of values, containers, and mathematical operators whereas  the statement is just like a 
command that a python interpreter executes like print.


# In[15]:


#6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1


# In[18]:


#7. What should the values of the following two terms be?
'spam'+'spamspam'


# In[19]:


'spam'*3


# In[ ]:


#So both are same 


# In[ ]:


#8. Why is eggs a valid variable name while 100 is invalid?
 we can't start giving variable an integer name.
if we, we should begin with, a string-like alphabet name then integer. e100 or eggs100 is valid


# In[ ]:


get_ipython().set_next_input('9. What three functions can be used to get the integer, floating-point number, or string version of a value');get_ipython().run_line_magic('pinfo', 'value')

ans: str(), int(), float()


# In[ ]:


get_ipython().set_next_input('10. Why does this expression cause an error? How can you fix it');get_ipython().run_line_magic('pinfo', 'it')

'I have eaten' + 99 + 'burritos' 

sol:  because 99 is an integer it cannot be concatenated with strings, if we have to concatenate it we need to do typecasting.

