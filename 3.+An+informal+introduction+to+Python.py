
# coding: utf-8

# # 3.1 Using python as a calculator
# ## 3.1.1. Numbers
# Operators +, -, *, and / are normal, with () used for grouping.
# 
# 

# In[8]:


2+2


# In[9]:


50 - 5*6


# In[10]:


(50 - 5*6)/4


# In[11]:


8/5 # division always returns a floating point


# Integer numbers have type int, fractional part have type float. 

# In[12]:


17/3 #float 


# In[13]:


17//3 #floor division discards fraction


# In[14]:


17%3 #% operator returns remainder


# In[15]:


5*3+2 #result * divisor +remainder


# ** operator calculates powers

# In[16]:


5**2 #5 squared


# In[17]:


2**7 #2 to the power of 7 


# In[18]:


width = 20 
height = 5*9


# If a variable is not assigned a value, it will error

# In[19]:


n


# there is full support for floating poing (example: 5.66666); operators with mixed type operands convert the integer operand to floating point. 

# In[20]:


4* 3.75 -1


# last printe expression is assigned to the variable _. This means that when you are using python as a desk calculator, it is somewhat easier to continue calculations. 
# 

# In[22]:


tax = 12.5/100
price = 100.5
price * tax


# In[23]:


price + _ #<-


# In[24]:


round(_, 2) #<- continues calculations by inserting previous output


# In addition to int and float, python supports other types of numberes such as Decimal and Fraction. Python also has built-in support for complex numbers, and uses the j or J suffix to indicatethe imagineary part (e.g. 3+5j)
# 

# ## 3.1.2. String
# Manipulate strings, which can be expressed in several ways. They can be enclosed in single quotes ('...') or double quotes ("...") with the same result. \ can be used to escape quotes. 

# In[25]:


'spam eggs' # single quotes


# In[27]:


'doesn\'t' #'\ escapes single quote


# In[29]:


'"Yes,"he said.'


# In[30]:


"\"Yes,\" he said."


# In[31]:


'"Isn\'t," she said.'


# In[33]:


'"Isn\'t," she said.'
print('"Isn\'t," she said.')


# In[34]:


s = 'first line. \nSecond line.' # \n means new line
s


# In[35]:


print(s)


# In[36]:


print('C:\some\name')


# In[37]:


print(r'C:\some\name') #r is raw springs


# In[39]:


print ("""Usage: thingy [OPTIONs]
    -h
    -H hostname
""")


# In[40]:


3*'un' +'ium'


# In[43]:


'py''thon'


# In[45]:


text = ('Put several strings within parentheses''tohave them joined together.')
text


# In[46]:


prefix = 'py'
prefix 'thon' #can't concatenate a variable


# In[47]:


('un' *3) 'ium'


# In[50]:


prefix = 'py'


# In[51]:


prefix +'thon'


# Strings can be indexed (subscripted) with the first character having index 0. There is no seperate character type; a character is simply a string of size one. 

# In[52]:


word = 'python'


# In[53]:


word[0] 


# In[54]:


word[5]


# In[55]:


word [-1]


# In[56]:


word [-2]


# In[57]:


word[-6]


# slicing allows you to obtain substring

# In[58]:


word[0:2]


# In[59]:


word[2:5]


# s[:i]+s[i:]=s

# In[62]:


word[:2]


# In[63]:


word[4:]


# In[64]:


word[-2:
]


# In[65]:


word[42]


# In[66]:


word[4:42]


# In[67]:


word[42:]


# Python strings are immutable

# In[68]:


word[0] = 'J'


# In[69]:


word[2:]


# In[70]:


'J'+word[1:]


# In[72]:


word[:2]+'py'


# len() returns the length of a string

# In[75]:


s = 'supercalifragilisticexpialidocious'


# In[77]:


len(s)


# 
# ### Text Sequence Type — str
#     Strings are examples of sequence types, and support the common operations supported by such types.
# ### String Methods
#     Strings support a large number of methods for basic transformations and searching.
# ### Formatted string literals
#     String literals that have embedded expressions.
# ### Format String Syntax
#     Information about string formatting with str.format().
# ### printf-style String Formatting
#     The old formatting operations invoked when strings are the left operand of the % operator are described in more detail here. 

# # 3.1.3 Lists
# Lists can be written as a list of comma-seperated values between square brackets. 
# 

# In[78]:


squares = [1,4,9,16,25]
squares


# In[79]:


squares[0] #indexing


# In[82]:


squares [-1] #indexing


# In[84]:


squares [-3:] #slicing


# In[85]:


squares[:] #new shallow copy of list


# In[86]:


squares + [36,49, 64, 81, 100]


# In[87]:


cubes = [1, 8, 27, 65, 125]


# In[88]:


4**3


# In[89]:


cubes[3] = 64 #strings are immutable HOWEVR lists are mutable, meaning it is possible to change their content.


# In[90]:


cubes


# In[91]:


cubes.append(216)


# In[92]:


cubes.append(7**3)


# In[93]:


cubes


# In[94]:


letters = ['a','b','c','d','e','f','g']


# In[95]:


letters


# In[96]:


letters[2:5] = ['C','D','E']


# In[97]:


letters


# In[98]:


letters[2:5] = []


# In[99]:


letters


# In[102]:


letters[:]=[] # [:]=[] replaces all elements


# In[101]:


letters


# In[103]:


letters = ['a','b','c','d']


# In[105]:


len(letters) #len() counts how many in the list


# It is possible to nest lists (create lists containing other lists)

# In[106]:


a = ['a','b','c']
n = [1,2,3]
x = [a,n]
x


# In[107]:


x[0]


# In[108]:


x[0][1]


# ## 3.2. First steps towards programming
# initial sub-sequence Fibonacci series 

# In[109]:


a, b = 0,1
while a < 10:
    print (a)
    a, b = b, a+b


# - first line contains a multiple assignment. on the last line this is used again, demonstrating that the expressions on the right-hand side are all evaluated first before any of the assignents take place. The right-hand side expressions are evaluated from the left to the right.
# - the while loop executes as long as the condition a<10 remains true. Any non-zero integer value is true, zero is false. The condition may also be a string or list value, in fact ay sequence; are false. The test used in the example isa simple comparison. The standard comparison operators are written the same as in C: < (less than), >(greater than), ==(equal to), <=(less than or equal to), >=(greater than or equal to) and !=(not equal to)
# - the body of te loop is indented: indentation is python's way of grouping statements. At the interactive prompt, you have to type a tab or space(s) for each indented line. In practice you will prepare more complicated input for Python with a text editor; all decent text editors have an auto-indent facility. When a compound statement is entered interactively. it must be followed by a black line to indicate completion ( since the parser cannot guess when you have typed the last line.) Note that each line within a basic block must be indented by the same amount. 
# - The print() function writes the value of the arguents(s) it is given. It differs from just writing the expression yo want to write in the way it handles multiple arguments, floating point quantities, and strings. Strings are printed without quotes, and a space is inserted between items, so you can format things nicely, like this:

# In[110]:


i = 256*256
print('The value of i is', i)


# The keyword argument end can be used to avoid the newline after the output, or end the output with a different string.

# In[112]:


a, b = 0, 1
while a < 1000:
    print(a, ',')
    a, b = b, a+b


# In[113]:


a, b = 0,1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b


# # Footnotes:
# 1. Since ** higher precedence than -, -3**2 will be -(3**2) result in -9. To avoid this and get 9, you can use (-3)**2
# 2. \n have the same meaning with both single '...' and double "..." quotes. The only difference between the two is that within single quotes you don't need to escape " ( but you have to escape \') and vice versa
