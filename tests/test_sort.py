#!/usr/bin/env python
# encoding: utf-8
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

from ds import sort

class TestSort(unittest.TestCase):
    def testQuicksort(self):
        data = [ 3, 6, 4, 1, 8, 3, 6, 4, 87, 54, 37,54 ,19, 345]
        sorted_data = sorted(data)
        data = sort.quicksort(data)

        self.assertEquals(sorted_data, data)


    def testHeapsort(self):
        data = [ 3, 6, 4, 1, 8, 3, 6, 4, 87, 54, 37,54 ,19, 345]
        sorted_data = sorted(data)
        sort.heapsort(data)

        self.assertEquals(sorted_data, data)

    def testMergesort(self):
        data = [ 3, 6, 4, 1, 8, 3, 6, 4, 87, 54, 37,54 ,19, 345]
        sorted_data = sorted(data)
        data = sort.mergesort(data)

        self.assertEquals(sorted_data, data)

    def testBigArray(self):
        data = [ random.randint(1, 100000) for i in range(10000)]
        sorted_data = sorted(data)

        qdata = list(data)
        qdata = sort.quicksort(qdata)
        self.assertEquals(sorted_data, qdata)

        hdata = list(data)
        sort.heapsort(hdata)
        self.assertEquals(sorted_data, hdata)

        mdata = list(data)
        mdata = sort.mergesort(mdata)
        self.assertEquals(sorted_data, mdata)
