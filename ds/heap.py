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


class Heap:
    """A heap efficiently supports the following operations:
    
        Insert(e)
        e = ExtractMax()
        
        It maintains the heap invariant, which that the children of any
        element are less that the element."""
        
    def __init__(self, contents=[]):
        """Create a new, empty Heap.
        
        To make it more pythonic we use a 0-indexed structure"""
        self._heap = contents
        
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

    def _siftup(self, pos):
        """given a position in heap, sift that element up to it's correct place"""
        parent = (pos - 1) >>1
        while pos and self._heap[pos] > self._heap[parent]:    
            self._heap[pos], self._heap[parent] = self._heap[parent], self._heap[pos]
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
            self._heap[startpos], self._heap[largest] = self._heap[largest], self._heap[startpos]
            self._siftdown(largest, endpos)
        
        
    def __len__(self):
        return self._heap.__len__()    
        
    def __repr__(self):
        return self._heap.__repr__()
    