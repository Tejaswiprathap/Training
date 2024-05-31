#!/usr/bin/env python
# coding: utf-8

# # LINKED LIST 

# In[14]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return self.data
class Linkedlist:
    def __init__(self,nodes=None):
        self.head=None
        if nodes is not None:
            node=Node(data=nodes.pop(0))
            self.head=node
            for elem in nodes:
                node.next=Node(data=elem)
                node=node.next
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    def __repr__(self):
        node=self.head
        nodes=[]
        while node is not None:
            nodes.append(node.data)
            node=node.next
        nodes.append("None")
        return "->".join(nodes)
    def add_last(self,node):
        if self.head is None:
            self.head=node
            return
        for current_node in self:
            pass
        current_node.next=node
        


# In[15]:


llist=Linkedlist()
llist
first_node=Node('mehhh')
llist.head=first_node
llist

second_node=Node('moooo')
third_node=Node('boww')
forth_node=Node('meoww')
first_node.next=second_node
second_node.next=third_node
third_node.next=forth_node
llist


# In[16]:


llist=Linkedlist(['Tejaswi','Varshitha'])
llist.add_last(Node('Maniswar'))
llist


# # Cheap Travel

# In[17]:


'''Ann has recently started commuting by subway. We know that a one ride subway ticket costs a rubles.
Besides, Ann found out that she can buy a special ticket for m rides (she can buy it several times). 
It costs b rubles. Ann did the math; she will need to use subway n times. Help Ann, tell her what is the minimum sum of 
money she will have to spend to make n rides?'''


# In[18]:


#input
#6 2 1 2
#output
#6


# In[19]:


n,m,a,b=list(map(int,input().split()))
if m*a<=b:
    print(n*a)
else:
    print((n//m)*b+min((n%m)*a,b))


# In[20]:


# swap 2 elements in linked list
# prompt: swap 2 elements in linked list

# prompt: swap 2 elements in linked list

def swap_nodes(linkedlist, node1, node2):
  prev1 = None
  curr1 = linkedlist.head
  while curr1 is not None and curr1.data != node1:
    prev1 = curr1
    curr1 = curr1.next
  prev2 = None
  curr2 = linkedlist.head
  while curr2 is not None and curr2.data != node2:
    prev2 = curr2
    curr2 = curr2.next
  if curr1 is None or curr2 is None:
    return
  if prev1 is None:
    linkedlist.head = curr2
  else:
    prev1.next = curr2
  if prev2 is None:
    linkedlist.head = curr1
  else:
    prev2.next = curr1
  curr1.next, curr2.next = curr2.next, curr1.next
  return linkedlist
swap_nodes(llist, 'Tejaswi', 'Varshitha')
llist


# In[24]:


#input: 647 667
#output: 1->3->1->4

#input: 56 1000
#output: 1->0->5->6
n1,n2=input().split()
ll1=Linkedlist(list(n1))
ll2=Linkedlist(list(n2))
print(ll1)
print(ll2)


# In[ ]:




