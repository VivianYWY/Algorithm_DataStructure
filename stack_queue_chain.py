# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 15:37:21 2018

@author: moonl
"""

class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
q = Queue()
q.enqueue(4)

# pass potato to next person, when count num is done, the person who has potato will be deleted, untill only one person left finally
def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
        
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
            
        simqueue.dequeue()
    
    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

# Deque (self-defined)

class Deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        self.items.append(item)
        
    def addRear(self, item):
        self.items.insert(0,item)
        
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

# palchecker
        
def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)
        
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last =  chardeque.removeRear()
        if first != last:
            stillEqual = False
            
    return stillEqual

print(palchecker("isdkjssk"))


# chain

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext

temp = Node(93)

# unordered list

class UnorderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found 


        


    