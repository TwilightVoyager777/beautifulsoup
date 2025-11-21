# Milestone-4

## Overview
In this milestone4, we extend the BeautifulSoup class so that a Soup object
becomes an iterable object. Iteration should traverse the underlying parse tree
in a streaming, depth-first manner, without collecting nodes into a list.

We added the method:

BeautifulSoup.__iter__(self)

in __init__.py.

This method performs a DFS traversal by using an explicit stack. Tag nodes,
text nodes, and comments are all produced one by one.

### Test
```bash
  pytest bs4/tests/test_iterable.py -q
```

### Task
```bash
  python apps/m4/m4.py apps/Posts.xml
```
