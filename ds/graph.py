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
"""
Graph structures and algorithms.

"""

class UniGraph:
    """
    Defines a generic undirected graph, based on adjacency lists.


    """
    def __init__(self, node_count, edges = None):
        """Create a new graph with the given number of vertices.

        Parameters:
        node_count : The number of vertices in the graph (required)

        edges: a list of edges, expressed as (i,j) pairs
               where i, j are 0-indexed indices of the
               vertices.  (optional)
        """
        self.vertexes = [ [] for v in range(node_count)]
        if edges:
            for edge in edges:
                self.add(edge)

    def add(self, edge):
        """Add an edge to the graph.

        Parameters:
        edge: a 2-tuple (i,j)
        """
        i, j = edge
        if j not in self.vertexes[i]:
            self.vertexes[i].append(j)
            self.vertexes[j].append(i)

    def __str__(self):
        """Print out representation of graph."""
        return "[Graph: n=%d, m=%d]" % self.size()


    def __len__(self):
        return len(self.vertexes)

    def size(self):
        """Return a tuple of (n, m) for the graph."""
        return len(self.vertexes), sum([len(v) for v in self.vertexes])

    def neighbours(self, vertex):
        """Return the list of neighbours of vertex

        Parameters:
        vertex: the vertex in question

        Returns: a list containing the vertex IDs.

        Raises: IndexError if the vertex is out of range of the graph"""
        return list(self.vertexes[vertex])
