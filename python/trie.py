# Copyright (C) 2011 Simon Otter
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE Simon Otter BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
# 
# Except as contained in this notice, the name of the Simon Otter shall
# not be used in advertising or otherwise to promote the sale, use or
# other dealings in this Software without prior written authorization
# from Simon Otter.

#
# Trie module
# By Simon Otter 2011
#

# Notes:
#   Only tested in Python 3k.
#

"""Trie module. Note that one cannot remove sequences
from Tries at the moment."""

class Node(dict):
    """Represents a Trie-node, this class is
    a utility for the Trie class.
    """
    def __init__(self):
        self.__end = False
    
    @property
    def is_end(self):
        return self.__end
    
    @is_end.setter
    def is_end(self, value):
        self.__end = value
        
    def __repr__(self):
        s = "*" if self.is_end else ""
        for k,v in self.items():
            s += "{0}:\n\t{1}".format(k, v)
        return s

class Trie:
    """A Trie which allows insertion and simple querying."""

    def __init__(self):
        self.__root = Node()
    
    def insert(self, seq):
        """Inserts a sequence into the trie.

        >>> t = Trie()
        >>> t.insert("Carl Sagan")
        >>> t.insert("Carl Bildt")
        >>> t.insert("")
        >>> t.insert([1, 2, 3])
        >>> t.contains("Carl Bildt")
        True
        """
        seq = list(seq)
        if not seq:
            return
        
        node = self.__root
        for el in seq:
            child = node.get(el)
            if child == None:
                child = Node()
            
            node[el] = child
            node = child

        node.is_end = True

    def contains(self, seq):
        """Checks if the trie contains a given string.
        
        >>> t = Trie()
        >>> t.insert("Carl Sagan")
        >>> t.contains("Carl Sagan")
        True
        >>> t.insert([1, 2, 3])
        >>> t.contains([1, 2])
        False
        >>> t.contains([1, 2, 3])
        True
        """
        seq = list(seq)
        if not seq:
            return False
        
        node = self.__root

        for el in seq:
            child = node.get(el)
            if child == None:
                return False
            
            node = child
        
        return node.is_end
    
    def find_by_prefix(self, seq):
        """Finds all strings matching a prefix.

        Note that strings put in we'll be returned
        as sequences, you'll need to flatten them
        manually with str.join.

        >>> t = Trie()
        >>> t.insert([1, 2, 3])
        >>> t.insert([1, 2, 4, 5])
        >>> t.insert([2, 9])
        >>> list(t.find_by_prefix([1, 2]))
        [[1, 2, 3], [1, 2, 4, 5]]
        >>> list(t.find_by_prefix([1, 2, 5]))
        []
        >>> list(t.find_by_prefix([1, 2, 3]))
        [[1, 2, 3]]
        >>> t.find_by_prefix([])
        Traceback (most recent call last):
            ...
        ValueError: expected a non empty iterable
        """
        seq = list(seq)
        if not seq:
            raise ValueError("expected a non empty iterable")
        
        matches = []

        read = []
    
        node = self.__root
        for el in seq:
            child = node.get(el)
            if child == None:
                return []
            
            read.append(el)
            node = child
        
        # node now points to the node for the last
        # element in the prefix.

        def find_children(n, r):
            if n.is_end:
                matches.append(r)
            for k,v in n.items():
                find_children(v, r + [k])
        
        find_children(node, read)

        return matches

def trie(*seqs):
    """Creates a new Trie and inserts
    all the parameters into the trie.

    >>> t = trie("hello", "hallå")
    >>> t.contains("hello")
    True
    >>> t.contains("hallå")
    True
    >>> t.contains("tofu")
    False
    """
    t = Trie()
    for s in seqs:
        t.insert(s)
    return t

if __name__ == "__main__":
    import doctest
    doctest.testmod()