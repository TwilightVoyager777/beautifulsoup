# Milestone-2

## Milestone 2 — Part 1 : SoupStrainer Applications
Large test file: **Posts.xml** (≈ 1.4 GB)
### Execution Details
Task 2 – Extract all hyperlinks
```bash
  time python apps/m2/task2.py apps/Posts.xml
```
Runtime: 17.72s user 2.48s system 92% cpu 21.750 total

Task 3 – List all tag names
```bash
  time python apps/m2/task3.py apps/Posts.xml
```
Runtime:  28.19s user 8.63s system 53% cpu 1:09.37 total

Task 4 – Print all tags containing an id attribute
```bash
  time python apps/m2/task4.py apps/Posts.xml
```
Runtime:  28.60s user 7.22s system 54% cpu 1:06.08 total


## Milestone 2 — Part 2 : Source Locations

---

### M1-Task1 – Read → Parse → Prettify
| API / Method | Source File | Line |
|---------------|--------------|------|
| BeautifulSoup.__init__ | bs4/__init__.py | L133 |
| Tag.prettify | bs4/element.py | L2601 |

---

### M1-Task2 – Extract All Hyperlinks (`<a>` tags)
| API / Method | Source File | Line |
|---------------|--------------|------|
| Tag.find_all | bs4/element.py | L2715 |
| Tag.get | bs4/element.py | L2203 |

---

### M1-Task3 – List All Tag Names
| API / Method | Source File | Line |
|---------------|--------------|------|
| Tag.find_all | bs4/element.py | L2715 |
| Tag.name | bs4/element.py | L1648 |

---

### M1-Task4 – Tags with ID Attribute (Single API Call)
| API / Method | Source File | Line |
|---------------|--------------|------|
| Tag.find_all | bs4/element.py | L2715 |
| Tag.attrs | bs4/element.py | L1682 |

---

### M1-Task5 – Parent Lookup / CSS Selectors
| API / Method | Source File | Line |
|---------------|--------------|------|
| Tag.find_parent | bs4/element.py | L992 |
| Tag.select | bs4/element.py | L2799 |

---

### M1-Task6 – Replace `<b>` with `<blockquote>`
| API / Method | Source File | Line |
|---------------|--------------|------|
| Tag.find_all | bs4/element.py | L2715 |
| Tag.name | bs4/element.py | L1648 |
| Tag.prettify | bs4/element.py | L2601 |

---

### M1-Task7 – Add or Replace `class="test"` in All `<p>` Tags
| API / Method | Source File | Line |
|---------------|--------------|------|
| Tag.find_all | bs4/element.py | L2715 |
| Tag.attrs | bs4/element.py | L1682 |

---

### M1-Task8 – Extract Plain Text
| API / Method | Source File | Line |
|---------------|--------------|------|
| Tag.get_text | bs4/element.py | L524 |

---

### M2 – Part 1 (SoupStrainer Applications for Tasks 2 – 4)
| API / Method | Source File | Line |
|---------------|--------------|------|
| BeautifulSoup.__init__ | bs4/__init__.py | L133 |
| SoupStrainer | bs4/filter.py | L313 |
| Tag.find_all | bs4/element.py | L2715 |
| Tag.get | bs4/element.py | L2203 |
| Tag.name | bs4/element.py | L1648 |

---

## Milestone 2 — Part 3 : SoupReplacer
```bash
  python apps/m2/task6.py apps/Posts.xml
```