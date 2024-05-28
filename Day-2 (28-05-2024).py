#!/usr/bin/env python
# coding: utf-8

# # check if a num is prime or not

# In[1]:


num=int(input())
count=0
for i in range(1,num+1):
  if num % i==0:
    count+=1
if count==2:
  print("prime")
else:
  print("not a prime")


# In[2]:


#method2 
num=int(input())
for deno in range(2,(num//2)+1):
  if num % deno==0:
    print("not prime")
    break
else:
  print("prime")


# In[3]:


#method3
num=int(input())
for deno in range(2,num):
  if num % deno ==0:
    print("not prime")
    break
else:
  print("prime")


# In[4]:


#method4
num=int(input())
for deno in range(2,int(num**0.5)+1):
  if num % deno==0:
     print("not prime")
     break
else:
  print("prime")


# # give an integer n , return true if it is a power of 6 ,otherwise return false

# In[6]:


n=int(input())
while n % 6==0:
  n=n//6
if n==1:
  print("true")
else:
  print("false")


# # n=5
# # output 5 4 3 2 1 using recursion

# In[7]:


def rec(n):
  if n==0:
    return
  print(n,end=" ")
  rec(n-1)
rec(5)


# In[8]:


#or
def greet(n):
  if n<=0:
    return
  print("hello")
  greet(n-1)
greet(5)


# # op: 1 2 3 4 5

# In[9]:


def rec(n):
  if n==0:
    return
  rec(n-1)

  print(n,end=" ")
rec(5)


# # print the string in reverse order using recursion

# In[10]:


strData=" why are you shy"
def revStr(data):
  if data=="":
    return data
  return data[-1]+revStr(data[:-1])
print(revStr(strData))


# # '123' ->true
# # '123a' -> false

# In[11]:


import string
strNum=input()
for i in strNum:
  if i not in string.digits:
    print("false")
    break
else:
  print("true")


# # generate a num from the given string ,if no digit found return 0
# # 123av45b78 ->12345678 ->[int]

# In[12]:


import string
strNum=input()
num=""
for i in strNum:
  if i in string.digits:
    num+=i
print(int(num))
print(type(num))


# # swapcase

# In[5]:


print('hElLo'.swapcase())


# In[13]:


str1="welcome"
print(str1*2)


# In[14]:


print(str1[:6]+' Coder')


# # isdigit

# In[15]:


str1="is 2020"
str2="2020"
print(str1.isdigit())
print(str2.isdigit())


# # remove all consecutive duplicates from string

# In[17]:


def remove_duplicates(strr):
  res = []
  for i in range(len(strr)):
    if not res or strr[i] != res[-1]:
      res.append(strr[i])
  return ''.join(res)

strr = input()
obj= remove_duplicates(strr)
print(obj)


# In[19]:


#or
data=input()
res=data[0]
k=0
for i in range(1,len(data)):
    if data[i]!=res[k]:
        res+=data[i]
        k+=1
print(res)


# # input: carrace 

# In[ ]:


# no.of iterations 3(rotations)
# L 2(rotate left side 2 times) L- left rotation  R- right rotation
# R 2 
# L 3
# output: NO


# In[21]:


data=input()
rot=int(input())
res=''
for i in range(rot):
    di,mag=input().split()
    if di.upper()=='L':
        res+=(data[int(mag):]+data[:int(mag)])[0]
    elif di.upper()=='R':
        res+=(data[:int(mag)]+data[int(mag):])[0]
subList=[data[i:i+rot] for i in range(len(data))]
#Anagram
for subele in subList:
    if sorted(subele)==sorted(res):
        print("Yes")
        break
else:
    print("No")


# In[5]:


#or
from collections import deque
data=input()
qstr=deque(data)
rot=int(input())
res=''
for i in range(rot):
    di,mag=input().split()
    if di=='L' or di=='l':
       qstr.rotate(-int(mag))
       res+=qstr[0]
    elif di=='R' or di=='r':
        qstr.rotate(-int(mag))
        res+=qstr[0]
subList=[data[i:i+rot] for i in range(0,len(data)-rot+1)]
for subele in subList:
    if sorted(subele)==sorted(res):
        print("Yes")
        break
else:
    print("No")


# # join string

# In[6]:


strList=['w','e','l','c','o','m','e']
res=''.join(strList)
print(res)


# In[ ]:




