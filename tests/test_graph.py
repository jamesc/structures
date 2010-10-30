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

import unittest

from ds import graph

class TestGraph(unittest.TestCase):

    def test_ctor(self):
        g = graph.UniGraph(3, [ (0,1), (0,2)])
        self.assertEquals(3, len(g))
        self.assertEquals( (3,4), g.size())

        self.assertEquals([1,2], g.neighbours(0))
        self.assertEquals([0], g.neighbours(1))
        self.assertEquals([0], g.neighbours(2))

    def test_graph_ops(self):
        """test simple ops"""
        g = graph.UniGraph(10)

        self.assertEquals(10, len(g))

        for i in range(10):
            g.add( (i, (i+1)%10), ) # A loop

        for i in range(10):
            self.assertEquals(2, len(g.neighbours(i)))

        self.assertEquals( (10,20), g.size())
