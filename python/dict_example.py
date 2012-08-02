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

# This is just an example, which searches a dictionary
# by prefix.

# Do note that for large word lists this program will consume much 
# memory. We are not exactly space conserving here.

import trie
import time

"""Change this path to use another word list.
The word list should be of format:
 word1
 word2
 ...
 wordN
"""
dict_file = "../words/english-words-95.txt"

def build_trie():
    t = trie.Trie()
    with open(dict_file, "r") as f:
        for l in f:
            t.insert(l.strip())
    return t

def flatten_results(lst):
    return ("".join(x) for x in lst)

def main():
    print("Building word list, please wait...")
    t = None
    try:
        t = build_trie()
    except:
        print("Could not build word list.")
    print("Completed.")
    print()

    try:
        while True:
            text = input("find> ")
            
            ssec = time.clock()
            results = flatten_results(t.find_by_prefix(text))
            esec = time.clock()

            length = 0
            for word in results:
                print(word)
                length += 1

            print("Found {1} words. Query time about {0}s.".format(esec - ssec, length))
    except (KeyboardInterrupt, EOFError):
        print("Good bye man.")

if __name__ == "__main__":
    main()