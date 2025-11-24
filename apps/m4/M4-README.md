# Milestone-4

## Overview
In this milestone4, we extend the BeautifulSoup class so that a Soup object
becomes an iterable object. Iteration should traverse the underlying parse tree
in a streaming, depth-first manner, without collecting nodes into a list.

We added the method:

BeautifulSoup.__iter__(self)

in __init__.py.

This method performs a DFS traversal using a recursive generator.
Each node (tags, text nodes, and comments) is yielded one at a time during
traversal. No lists, stacks, or intermediate collections are created—
the iteration is fully streaming.

### Test
```bash
  pytest bs4/tests/test_iterable.py -q
```

### Task
```bash
  python apps/m4/m4.py apps/Posts.xml
```
