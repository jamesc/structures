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
Sorting algorithms
"""

from random import randrange

from ds.heap import Heap

__all__ = [ 'quicksort', 'heapsort', 'mergesort' ]

def quicksort(array):
    """
    Quicksort using list comprehensions and randomized pivot
    >>> quicksort<<docstring test numeric input>>
    <<docstring test numeric output>>
    >>> quicksort<<docstring test string input>>
    <<docstring test string output>>
    """
    def qsort(array):
        """We want to not perturbe the original list, so use this
        inner def."""
        if array == []:
            return []
        else:
            pivot = array.pop(randrange(len(array)))
            lesser = qsort([l for l in array if l < pivot])
            greater = qsort([l for l in array if l >= pivot])
            return lesser + [pivot] + greater
    return qsort(array[:])

def heapsort(array):
    """Implements heapsort in-place using heap.Heap.  Insert all
    the values in (via heapify in O(n) ) and the read them
    out in max order, inserting into the correct place in the
    orig list
    """

    heapy = Heap(array)
    for i in reversed(range(len(array))):
        array[i] = heapy.extract_max()


def _merge(left, right):
    """Merge two lists and return the merged result
    """
    result = []

    while len(left) or len(right):
        if len(left) and len(right):
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left):
            result.extend(left)
            left = []
        elif len(right):
            result.extend(right)
            right = []
    return result

def mergesort(array):
    """Implements mergesort."""
    size = len(array)
    if size <= 1:
        return array
    left = array[:size/2]
    right = array[size/2:]

    left = mergesort(left)
    right = mergesort(right)
    return _merge(left, right)