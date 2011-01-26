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
Heaps and Priority Queues
"""

class Heap:
    """A (max-)heap efficiently supports the following operations:

        Insert(e)
        e = ExtractMax()
        e = replace(new_e)
        It maintains the heap invariant, which that the children of any
        element are less that the element."""

    def __init__(self, contents=None):
        """Create a new, empty Heap.

        To make it more pythonic we use a 0-indexed structure
        """
        if contents:
            self._heap = list(contents) # copy it
            self._heapify()
        else:
            self._heap = []

    def insert(self, elem):
        """Insert an element into the heap, growing it by 1."""
        pos = len(self._heap)
        self._heap.append(elem)
        self._siftup(pos)

    def find_max(self):
        """Return the maximum element in the heap"""
        return self._heap[0]

    def extract_max(self):
        """Remove and return the maximum element from a heap, maintaining the
        heap invariant."""

        lastelt = self._heap.pop() # Raises IndexError on empty heap
        if self._heap:
            returnitem = self._heap[0]
            self._heap[0] = lastelt
            self._siftdown(0, len(self._heap))
        else:
            returnitem = lastelt
        return returnitem

    def replace(self, elem):
        """Remove the max and replace it with the supplied element.
        Note that the value returned could be less than the one
        supplied.  Should be used in code e.g

        if elem < heap.find_max():
            elem = heap.replace(elem)

        """
        returnitem = self._heap[0] # return IndexError if heap is empty
        self._heap[0] = elem
        self._siftdown(0, len(self._heap))
        return returnitem

    def _siftup(self, pos):
        """given a position in heap, sift that element up to it's
        correct place"""
        parent = (pos - 1) >>1
        while pos and self._heap[pos] > self._heap[parent]:
            self._heap[pos], self._heap[parent] \
                    = self._heap[parent], self._heap[pos]
            pos = (pos - 1) >> 1
            parent = (pos -1) >> 1

    def _siftdown(self, startpos, endpos):
        """Given a new element at startpos, sift it down until it
        sits at the correct place"""
        left = 2 * startpos + 1
        right = left + 1
        largest = startpos

        if left < endpos and self._heap[left] > self._heap[startpos]:
            largest = left
        if right < endpos and self._heap[right] > self._heap[largest]:
            largest = right
        if largest > startpos:
            self._heap[startpos], self._heap[largest] \
                    = self._heap[largest], self._heap[startpos]
            self._siftdown(largest, endpos)

    def _heapify(self):
        """Given a unheaped lst, heapify it in O(n)."""
        endpos = len(self._heap) / 2
        for idx in reversed(xrange(endpos)):
            self._siftdown(idx, len(self._heap))

    def __len__(self):
        return self._heap.__len__()

    def __repr__(self):
        return self._heap.__repr__()

