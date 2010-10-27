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

from ds.heap import Heap

__all__ = [ 'quicksort', 'heapsort', 'mergesort' ]

def _partition(array, left, right, pivot):
    """Do the partition step of quicksort

    array:  the array to be sorted
    the section (left, right - 1) of the array will
    be pivoted around the index 'pivot'

    Returns:
       The new index of the value which was at pivot
    """
    pivot_val = array[pivot]
    array[pivot], array[right] = array[right], array[pivot]
    store = left
    for i in range(left, right):
        if array[i] <= pivot_val:
            array[i], array[store] = array[store], array[i]
            store += 1
    array[store], array[right] = array[right], array[store]
    return store


def quicksort(array, left=0, right=-1):
    """Implements quicksort in-place on a fixed length array
    """
    if right is -1:
        right = len(array) - 1

    while right > left:
        pivot = left + (right - left) / 2
        new_pivot = _partition(array, left, right, pivot)
        # Recurse into smaller, tail call into larger
        # to avoid stack overflow
        if new_pivot - left < right - new_pivot:
            quicksort(array, left, new_pivot - 1)
            left = new_pivot + 1
        else:
            quicksort(array, new_pivot + 1, right)
            right = new_pivot - 1

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