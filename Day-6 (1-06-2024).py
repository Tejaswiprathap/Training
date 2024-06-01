#!/usr/bin/env python
# coding: utf-8

# # palindrome using stack

# In[3]:


# input: string
#output: print palindrome if string is palindrome , else print not a palindrome
strData=input()
stack=list(strData)
#print(stack)
for i in strData:
    if stack.pop()!=i:
        print("Not a palindrome")
        break
else:
    print("Palindrome")


# # Valid Parentheses using stack

# In[13]:


#Input: s = "()[]{}"
#Output: true
#Input: s = "(]"
#Output: false
class Solution:
    def isValid(self,s:str)->bool:
        stack=[]
        for i in s:
            if i=='(':
                stack.append(')')
            elif i=='{':
                stack.append('}')
            elif i=='[':
                stack.append(']')
            elif not stack or stack.pop()!=i:
                return False
        return "not stack"
s=input()
obj=Solution()


# # JNEXT 

# In[ ]:


'''Input:
2
5
1 5 4 8 3
10
1 4 7 4 5 8 4 1 2 6

Output:
15834
1474584162'''


# In[8]:


t=int(input())
for i in range(t):
    n=int(input())
    numList=list(map(int,input().split()))
    index=n-1
    for i in range(n-1,0,-1):
        if numList[i]>numList[i-1]:
            numList[i],numList[i-1]=numList[i-1],numList[i]
            index=i
            break
    res=[str(ele) for ele in (numList[:index]+(numList[index:])[::-1])]
    a=''.join(res)
    print(a)
    if a==numList:
        print('number is not possible')


# In[14]:


dStr=input() #hhoowaaaareyyoouu
stack=[]
for i in dStr:
    if stack and stack[-1]==i:
        stack.pop()
    else:
        stack.append(i)
print(''.join(stack))


# In[ ]:


'''Input
There are several test cases. The first line of each test case contains a single number n, the number of love mobiles.
The second line contains the numbers 1 to n in an arbitrary order. All the numbers are separated by single spaces. 
These numbers indicate the order in which the trucks arrive in the approach street. No more than 1000 love mobiles 
participate in the street parade. Input ends with number 0.

Output
For each test case your program has to output a line containing a single word "yes" if the love mobiles can be re-ordered
with the help of the side street, and a single word "no" in the opposite case.'''


# In[18]:


n=int(input())
trucks=list(map(int,input().split()))
side=[]
result=[]
for i in range(0,len(trucks)-1):
  if trucks[i]>trucks[i+1]:
    side.append(trucks[i])
  else:
    result.insert(0,trucks[i])
result.insert(0,trucks[-1])
result=side+result
print(result)
if sorted(trucks,reverse=True)==result:
  print("yes")
else:
  print("no")


# In[ ]:




