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
Binary Trees and Binary Search Trees
"""

class Node:
    """A tree node, holding a value and left/right child pointers"""

    def __init__(self, value, parent, left=None, right=None):
        """Create a new node, possible with pointers to left and right
        children and parent"""
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

class BinaryTree(object):
    """A Binary search tree."""

    def __init__(self, root=None):
        """Create a new Binary Tree.  Optionally provide a root node."""
        self.root = root
        
    
    def root(self):
        """Return the root of the tree.
        
        Returns `None` if the tree is empty.
        """
        return self.root
    
    def search