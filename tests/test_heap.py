"""
Copyright (c) 2010 CERN. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

    http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License.
"""

import unittest

from ds import heap

class TestHeap(unittest.TestCase):

    def test_insert(self):
        h = heap.Heap()
        h.insert(1)
        self.assertEquals([1], h._heap)
        
        h.insert(6)
        self.assertEquals([6, 1], h._heap)
        
        h.insert(10)
        self.assertEquals([10, 1, 6], h._heap)
        
        h.insert(3)
        self.assertEquals([10, 3, 6, 1], h._heap)
        
    def test_extractmax(self):
        h = heap.Heap()
        h.insert(1)
        self.assertEquals(1, h.find_max())
        h.insert(6)
        self.assertEquals(6, h.find_max())
        h.insert(10)
        self.assertEquals(10, h.find_max())
        h.insert(3)
        self.assertEquals(10, h.find_max())
        
        self.assertEquals(10, h.extract_max())
        self.assertEquals(6, h.extract_max())
        self.assertEquals(3, h.extract_max())
        self.assertEquals(1, h.extract_max())
        
        
    def test_heapsort(self):
        """Do a heapsort."""
        h = heap.Heap()
        data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
        for item in data:
            h.insert(item)
        sort = []
        while h:
            sort.append(h.extract_max())
        
        self.assertEquals([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], sort)
