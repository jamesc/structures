#!/usr/bin/env python
#
# Copyrigh CERN, 2010.
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

import sys
import os

import random
import time

from ds import sort

def main():
    data = [ random.randint(1, 10000) for i in range(1000)]
    start = time.time()
    sorted_data = sorted(data)
    end = time.time()
    print "Python Sort : %f"%(end-start)

    qdata = list(data)
    start = time.time()
    sort.quicksort(qdata)
    end = time.time()
    print "QuickSort   : %f"%(end-start)

    hdata = list(data)
    start = time.time()
    sort.heapsort(hdata)
    end = time.time()
    print "HeapSort    : %f"%(end-start)

    mdata = list(data)
    start = time.time()
    mdata = sort.mergesort(mdata)
    end = time.time()
    print "MergeSort   : %f"%(end-start)

if __name__ == '__main__':
    main()

