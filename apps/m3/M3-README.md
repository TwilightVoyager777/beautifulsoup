# Milestone-3

## Milestone 3 — SoupReplacer API Extension
Large test file: **Posts.xml** (≈ 1.4 GB)

### Constructors
```python
# Milestone 2 (basic)
SoupReplacer(og_tag, alt_tag)

# Milestone 3 (extended)
SoupReplacer(name_xformer=None, attrs_xformer=None, xformer=None)
```
### Test
```bash
  pytest bs4/tests/test_m3replacer.py -q
```

### Task7
```bash
  python apps/m3/task7.py apps/Posts.xml
```

## Technical brief outlining
In Milestone 2, the SoupReplacer API was simple but rigid — it only supported one-to-one tag name replacement.

Milestone 3 introduces a more complex but flexible functional design that allows users to transform tag names, attributes, or even modify nodes directly during parsing.

Although it adds a bit of complexity, the new interface is far more extensible and adaptable for future extensions.