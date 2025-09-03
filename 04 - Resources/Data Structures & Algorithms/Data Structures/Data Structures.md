---
tags:
  - DSA
date: 2025-08-18T12:23:00
---
An **array** is one of the most fundamental linear data structures. It is used to hold a collection of elements of the same type, arranged in a sequential manner. Arrays use **contiguous blocks of memory**, meaning that every element is stored right next to the previous one. Because of this property, arrays allow **direct access** to elements using their index, which makes operations like retrieval extremely efficient.

Arrays can be broadly divided into two categories:
- **One-dimensional arrays**: Data is stored in a simple linear list, with each element accessible by a single index.
- **Multi-dimensional arrays**: Data is stored in tabular or higher-dimensional form, such as matrices (2D) or even 3D arrays. These are essentially arrays of arrays.

---
## Characteristics of Arrays
- **Fixed Size**: The size of a static array is defined at the time of its creation and cannot change later.
- **Indexed Access**: Arrays support zero-based indexing, meaning the first element is at index `0`, the second at `1`, and so on.
- **Efficient Retrieval**: Accessing or updating an element at a given index takes constant time, i.e., **O(1)**.
- **Contiguous Memory Allocation**: Elements are laid out in adjacent memory locations, which improves cache performance and makes random access possible.
- **Homogeneous Data**: All elements must be of the same type (integers, floats, characters, etc.). `unless has a data type of []any. (check array snippets) `
---
## Static vs. Dynamic Arrays
- **Static Arrays**:
    - Declared with a fixed size at compile time.
    - The memory allocated cannot grow or shrink during execution.
    - Fast and memory-efficient since no resizing overhead exists.
    - Limitation: If the array is too small, it may not hold all the data; if it’s too large, memory is wasted.
    - Common in low-level programming languages like C or C++, where array sizes are usually determined beforehand.
- **Dynamic Arrays**:
    - Can grow or shrink in size during program execution.
    - Typically implemented with resizable structures that double their size when capacity is reached (e.g., `vector` in C++, `list` in Python, or `slice` in Go).
    - More flexible and user-friendly compared to static arrays.
    - Slightly less efficient due to resizing operations and potential memory reallocation.
    - Useful when the exact size of data is not known in advance.
---
## Advantages of Arrays
- Simple and easy to use.
- Random access provides constant time complexity for lookups.
- Memory locality (contiguous allocation) makes them cache-friendly and fast.
---
## Limitations of Arrays
- Fixed size (for static arrays) can cause inefficiency.    
- Insertion and deletion operations are costly since elements may need to be shifted, leading to **O(n)** time complexity.
- Memory may be wasted if the declared size is much larger than the actual number of elements needed.
---
## Static vs. Dynamic Arrays

| Feature                | Static Array                             | Dynamic Array                           |
| ---------------------- | ---------------------------------------- | --------------------------------------- |
| **Size**               | Fixed at declaration, cannot be changed  | Can grow or shrink during runtime       |
| **Memory Allocation**  | Contiguous, decided at compile time      | Contiguous, reallocated when resized    |
| **Flexibility**        | Rigid, not suitable when size is unknown | Flexible, good for unpredictable sizes  |
| **Performance**        | Very fast (no resizing overhead)         | Slight overhead during resizing         |
| **Insertion/Deletion** | Costly (requires shifting elements)      | Still costly, but resizing can help     |
| **Examples**           | C/C++ raw arrays                         | C++ `vector`, Python `list`, Go `slice` |

## Arrays in Memory
It is useful to first know how arrays are stored in memory.

Elements in an array are stored contiguously in memory. That means that each element is stored right after the previous element.

The image below shows how an array of integers myArray = [3,5,13,2] is stored in memory. We use a simple kind of memory here with two bytes for each integer, like in the previous example, just to get the idea.

![An array stored in memory](https://www.w3schools.com/dsa/img_linkedlists_arraymemory_new.png)

The computer has only got the address of the first byte of myArray, so to access the 3rd element with code myArray[2] the computer starts at `0x7F23` and jumps over the two first integers. The computer knows that an integer is stored in two bytes, so it jumps 2x2 bytes forward from `0x7F23` and reads value 13 starting at address `0x7F27`.

---
## Array snippets
See the full code examples here: [[Array Snippets]]
