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

from collections import deque

WHITE, GREY, BLACK = range(3)

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

    def has_edge(self, i, j):
        """Check if an edge i,j is in the graph

        """

        return j in self.vertexes[i]

    def neighbours(self, vertex):
        """Return the list of neighbours of vertex

        Parameters:
        vertex: the vertex in question

        Returns: a list containing the vertex IDs.

        Raises: IndexError if the vertex is out of range of the graph"""
        return list(self.vertexes[vertex])

    def size(self):
        """Return a tuple of (n, m) for the graph."""
        return len(self.vertexes), sum([len(v) for v in self.vertexes])

    def __str__(self):
        """Print out representation of graph."""
        return "[Graph: n=%d, m=%d]" % self.size()

    def __len__(self):
        return len(self.vertexes)


def components(graph):
    """Find and return the connected components of a graph

    Parameters:
    graph: A graph. It needs to support `neighbours(i) and len()

    Returns:  List of lists containing the vertices in each
    connected component"""

    result = []
    colour = [ WHITE for i in range(len(graph))]

    # use a stack to save on linear search through colour to find
    # next grey node
    grey = deque()
    for i in range(len(graph)):
        if colour[i] == WHITE:
            # Start new component
            component = []
            result.append(component)

            # Mark Grey
            colour[i] = GREY
            grey.append(i)
            while grey:
                j = grey.pop() # BFS
                for k in graph.neighbours(j):
                    if colour[k] == WHITE:
                        colour[k] = GREY
                        grey.append(k)
                # Add to component
                component.append(j)
                colour[j] = BLACK
    return result

def shortest_path(graph, start, end ):
    """Return the shortest path between two vertices in a graph.

    We do a BFS traversal of the graph, starting at `start`.  We keep a
    count of distance during the traversal for each visited node.

    After traversing the connected component containing `start` we will
    have either hit the node, or it's in a difference connected component."""
    if start > len(graph) or end > len(graph):
        return -1

    infinity = len(graph) + 1000 # Big enough
    distance = [ infinity for i in range(len(graph))]
    colour = [ WHITE for i in range(len(graph))]
    grey = deque()

    colour[start] = GREY
    grey.append(start)
    distance[start] = 0

    while grey:
        i = grey.popleft()
        for j in graph.neighbours(i):
            if colour[j] == WHITE:
                colour[j] = GREY
                grey.append(j)
                distance[j] = distance[i] + 1
        colour[i] = BLACK

    if distance[end] == infinity:
        return -1
    return distance[end]

