---
tags:
  - DSA
date: 2025-08-19T21:02:00
link: https://www.w3schools.com/dsa/dsa_data_stacks.php
---
A **stack** is a data structure that can hold many elements. **Stacks** operate on the Last-In-First-Out (LIFO) principle, where is the last element added to the *stack* is the first element to be removed. 

Think of a *stack* like a pile of pancakes.

In a pile of pancakes, the pancakes are both added and removed from the top. So when removing a pancake, it will always be the last pancake you added. This way of organizing elements is called LIFO: Last In First Out.

Basic operations we can do on a stack are:
- **Push:** Adds a new element on the stack.
- **Pop:** Removes and returns the top element from the stack.
- **Peek:** Returns the top element on the stack.
- **isEmpty:** Checks if the stack is empty.
- **Size:** Finds the number of elements in the stack.

Stacks can be implemented by using arrays or linked lists.

Stacks can be used to implement undo mechanisms, to revert to previous states, to create algorithms for depth-first search in graphs, or for backtracking.

---
## Application
During process execution in operating systems, memory is divided into "stack" and "heap". The stack portion of the memory is used whenever a function is called. Relevant data such as parameters, local variables, and return values are stored within a frame in a stack to be popped after the function has been completed. When an excessive number of function calls or an infinite recursive function are made, the computer's ability to store all of this information is exceeded. This results in the well-known stack overflow error.

---
## Stack Implementation using Arrays
Reasons to implement stacks using arrays:
- **Memory Efficient:** Array elements do not hold the next elements address like linked list nodes do.
- **Easier to implement and understand:** Using arrays to implement stacks require less code than using linked lists, and for this reason it is typically easier to understand as well.

A reason for **not** using arrays to implement stacks:
- **Fixed size:** An array occupies a fixed part of the memory. This means that it could take up more memory than needed, or if the array fills up, it cannot hold more elements.
---
## Stack Implementation using Linked Lists

A reason for using linked lists to implement stacks:
- **Dynamic size:** The stack can grow and shrink dynamically, unlike with arrays.

Reasons for **not** using linked lists to implement stacks:
- **Extra memory:** Each stack element must contain the address to the next element (the next linked list node).
- **Readability:** The code might be harder to read and write for some because it is longer and more complex.
---
## Stack snippets
See the full code examples here: [[Stack Snippets]]