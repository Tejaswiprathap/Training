#!/usr/bin/env python
# coding: utf-8

# # sum of all odd no.s from larger no.

# In[5]:


#ip:3446877846445566
def summ(n):
    count=0
    for i in n:
        if int(i)%2!=0:
            count+=int(i)
    return count
n=input()
print(summ(n))


# In[8]:


#or
#space complexity: around 12 bytes
#time complexity: O(n)
num=int(input())
totSum=0
while num!=0:
    rem=num%10
    if rem%2!=0:
        totSum+=rem
    num//=10
print(totSum)


# In[9]:


#or
#space complexity: 2n+8 which is 'n'
#time complexity: O(n)
num2=input()  
oddList=['1','3','5','7','9'] #oddStr='13579'
totalSum=0
for i in num2:
    if i in oddList:          #if i in oddStr
        totalSum+=int(i)
print(totalSum)


# # sort first half in asc and second half in desc in an array

# In[11]:


#ip: 1 21 5 2 50 16
#op: 1 2 5 50 21 16
numList=list(map(int,input().split()))
n=len(numList)
res=sorted(numList)[:n//2]
print(res)
res+=sorted(numList,reverse=True)[:n//2]
print(res)


# # Print a single integer, the number of crimes which will go untreated. 

# In[13]:


#input:
#no.of events
#crime occurred is represented by -1
#positive no. is no.of police recruited
num=int(input())
events=list(map(int,input().split()))
avaPolice=0
unEvents=0
for event in events:
    if event>0:
        avaPolice+=event
    elif event==-1:
        if avaPolice<=abs(event):
            unEvents+=abs(event)-avaPolice
            avaPolice=0
        else:
            avaPolice-=abs(event)
print(unEvents)


# # dividing watermelon into equal weights among 2 people (may not be in equal parts)

# In[14]:


weight=int(input())
if weight%2==0 and weight>2:
    print("YES")
else:
    print("NO")


# # reverse the given string keeping its special char at same place

# In[16]:


#input: h@ello
#output: o@lleh
def reverse_string_preserve_special_chars(s):
    alnum_chars = [c for c in s if c.isalnum()]
    reversed_alnum_chars = alnum_chars[::-1]
    
    result = []
    index = 0
    for char in s:
        if char.isalnum():
            result.append(reversed_alnum_chars[index])
            index += 1
        else:
            result.append(char)
    
    return ''.join(result)
input_string = input()
reversed_string = reverse_string_preserve_special_chars(input_string)
#print(input_string)
print(reversed_string)


# In[17]:


#or
import re
s=input()
s_list=re.findall("[a-zA-Z]",s)
s_list.reverse()
for i in range(len(s)):
    if(s[i]=='#'or s[i]=='@'):
        s_list.insert(i,s[i])
print(''.join(s_list))


# In[ ]:




