#
# Copyrigh Platform14, 2010.
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#
"""
Lists
"""

class Node(object):
    """A Doubly linked list element"""
    
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return "Node[%r|%s|%r]"% (self.prev, self.value, self.next)
        
class UnsortedLinkedList(object):
    """An unsorted doubly linked list."""
    
    def __init__(self):
        """Create a new, empty doubly linked list."""
        self.head = None
      
    def insert(self, value):
        """Insert the given `value` at the head of the list"""
        node = Node(value, prev=None, next=self.head)
        if self.head:
            self.head.prev = node
        self.head = node
    
    def _search(self, value):
        """Check if the list has an node with a given value.

        If so, return the node, otherwise `None`
        """
        node = self.head
        while node and node.value != value:
            node = node.next
        return node
        
    def search(self, value):
        """Check if the list has an node with a given value.

        If so, return `True`, otherwise `False`.
        """

        return self._search(value) != None
    
    def delete(self, value):
        """Delete a value from the list.  It should be a node which has been 
        returned by a method such as `search()`
        """
        
        node = self._search(value)
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
            
        if node.next:
            node.next.prev = node.prev
            
    def values(self):
        """Return as a list the values in the linked list"""
        values = []
        node = self.head
        while node:
            values.append(node.value)
            node = node.next
        return values