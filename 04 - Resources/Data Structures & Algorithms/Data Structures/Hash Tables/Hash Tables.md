---
tags:
  - DSA
date: 2025-08-20T14:26:00
---
Hash tables are a fundamental data structure that operates based on key-value pairs and enables constant-time operations for lookup, insertion, and deletion. Hash tables use immutable keys that can be strings or integers among other things. The following diagram shows a hash table that has integer keys and string values.
```
Hash table with integer keys and string values
 ┌─────┐       ┌─────┐
 │  1  ├─────► │ foo │
 └─────┘       └─────┘
 ┌─────┐       ┌─────┐
 │  2  ├─────► │ bar │
 └─────┘       └─────┘
 ┌─────┐       ┌─────┐
 │  3  ├─────► │ baz │
 └─────┘       └─────┘
```
---
A Hash Table is a data structure designed to be fast to work with.

The reason Hash Tables are sometimes preferred instead of arrays or linked lists is because searching for, adding, and deleting data can be done really quickly, even for large amounts of data.

In [[Linked Lists]], finding a person "Bob" takes time because we would have to go from one node to the next, checking each node, until the node with "Bob" is found.

And finding "Bob" in an [[04 - Resources/Data Structures & Algorithms/Data Structures/Arrays/Arrays|Arrays]] could be fast if we knew the index, but when we only know the name "Bob", we need to compare each element (like with Linked Lists), and that takes time.

With a Hash Table however, finding "Bob" is done really fast because there is a way to go directly to where "Bob" is stored, using something called a hash function.

---
### Hash Function
A **hash function** takes the key (for example, the string `"Bob"`) and converts it into an integer index that maps directly to a location in the underlying array.
- The same key always produces the same index (deterministic).
- Keys are spread evenly across the array (good distribution).
- The index is always within array bounds, usually by taking `hash(key) % array_size`.
---
### Collisions
Sometimes two different keys hash to the same index (e.g., `"Bob"` and `"Rob"` might both land on index 2). This is called a **collision**.
To handle this, hash tables use strategies like:
- **Chaining** → each index stores a linked list (or bucket) of all keys that hash there.
- **Open addressing** → if the desired index is taken, the table probes for the next free slot.
---
## Hash snippets
See the full code examples here: [[Hash Table Snippets]]