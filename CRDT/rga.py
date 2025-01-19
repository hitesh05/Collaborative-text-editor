import random
import numpy as np
import time
import copy

class Node:
    def __init__(self, data, timestamp):
        self.data = data
        self.timestamp = timestamp
        self.next = None
        self.back = None

class S4vector:
    def __init__(self, ssn, sid, vsum, seq):
        self.ssn = ssn
        self.sid = sid
        self.sum = vsum
        self.seq = seq
class RGA:
    def __init__(self,headnode):
        self.headnode = headnode
        self.timestamp = 0

    # Local Operations #
    def lfindlist(self, key):
        n = self.headnode
        i = 0
        while n != None:
            if n.data != None: # skip tombstones
                if key == i:
                    return n
            n = n.next # next node in linked list
            i+=1
        return None

    def lfindlink(self, n):
        if n.data == None: # if n is a tombstone
            return None
        else: 
            return n
        
    def linsert(self, i, data):
        refer_n = self.lfindlist(i) # if ith position doesn't exist, refer_n = None
        if refer_n == None:
            return False
        
        new_node = Node(data, self.timestamp+1) # ADD METHOD FOR TIMESTAMP
        self.timestamp += 1
        new_node.next = refer_n.next
        new_node.back = refer_n
        refer_n.next = new_node
        return True
    
    def ldelete(self, i):
        refer_n = self.lfindlist(i)
        if refer_n == None:
            return False
        
        refer_n.data = None # make node a tombstone
        return True

    def lupdate(self, i, data):
        refer_n = self.lfindlist(i)
        if refer_n == None:
            return False
        
        refer_n.data = data
        return True
    
    def lread(self, i):
        refer_n = self.lfindlist(i)
        if refer_n == None:
            return None
        
        return refer_n.data
    

def local_optest():
    rga = RGA(Node('c', 0))
    rga.linsert(0, 'a')
    rga.linsert(1, 'b')
    rga.linsert(2, 'd')
    rga.lupdate(0, 'e')
    rga.ldelete(1)

    for i in range(4):
        print(rga.lread(i))
