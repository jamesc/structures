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
import random

from ds import heap

class TestHeap(unittest.TestCase):

    def test_insert(self):
        h = heap.Heap()
        h.insert(1)
        self.check_invariant(h)

        h.insert(6)
        self.check_invariant(h)

        h.insert(10)
        self.check_invariant(h)

        h.insert(3)
        self.check_invariant(h)

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
        self.check_invariant(h)

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

    def test_heapify(self):
        """Create a Heap with a unheaped list of data"""
        data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
        h = heap.Heap(data)
        sort = []
        while h:
            sort.append(h.extract_max())

        self.assertEquals([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], sort)

    def test_empty_heap(self):
        """Check empty heap ops work as expected"""
        h = heap.Heap()

        self.assertRaises(IndexError, h.find_max)
        self.assertRaises(IndexError, h.extract_max)
        self.assertRaises(IndexError, h.replace, 1)
        self.assertFalse(h)
        self.assertEquals(0, len(h))

    def test_replace(self):
        """Check the replace operator works ok"""
        h = heap.Heap()
        for i in range(256):
            h.insert(random.random())
            self.check_invariant(h)
        for i in range(256):
            expected = h.find_max()
            result = h.replace(random.random())
            self.assertEquals(expected, result)
            self.check_invariant(h)

    def check_invariant(self, heap):
        for pos, item in enumerate(heap._heap):
            if pos: # 0th element has no parent
                parent = (pos - 1 ) >> 1
                self.assertTrue("Invariant good for pos %d"%pos, heap._heap[parent] >= heap._heap[pos] )