#!/usr/bin/env python
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


import unittest

from ds import list

class TestList(unittest.TestCase):
    def testInsertAndSearch(self):
        l = list.UnsortedLinkedList()
        
        self.assertFalse(l.search(1))
        
        l.insert(1)
        self.assertTrue(l.search(1))
        
        l.insert(2)
        l.insert(3)
        self.assertTrue(l.search(2))
        
        self.assertFalse(l.search(100))
        
    def testValues(self):
        """Check the prepending of elements"""
        
        l = list.UnsortedLinkedList()
        l.insert(1)
        l.insert(5)
        l.insert(2)
        l.insert(-1)
        # Values are in inverse insertion order
        self.assertEquals([-1,2,5,1], l.values())
        
    def testDeleteWhenEmpty(self):
        
        l = list.UnsortedLinkedList()
        
        l.insert(1)
        self.assertEquals([1,],l.values())
        l.delete(1)
        self.assertEquals([], l.values())
        
        
    def testDeleteFromStart(self):
        l = list.UnsortedLinkedList()

        l.insert(1)
        l.insert(2)
        l.insert(3)
        self.assertEquals([3,2,1],l.values())
        l.delete(3)
        self.assertEquals([2,1], l.values())        
        
    def testDeleteFromMiddle(self):
        l = list.UnsortedLinkedList()

        l.insert(1)
        l.insert(2)
        l.insert(3)
        self.assertEquals([3,2,1],l.values())
        l.delete(2)
        self.assertEquals([3,1], l.values())        
        
    def testDeleteFromEnd(self):
        l = list.UnsortedLinkedList()

        l.insert(1)
        l.insert(2)
        l.insert(3)
        self.assertEquals([3,2,1],l.values())
        l.delete(1)
        self.assertEquals([3,2], l.values())