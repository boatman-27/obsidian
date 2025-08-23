---
tags:
  - DSA
date: 2025-08-19T23:31:00
---
A **queue** is a data structure that can hold many elements. **Queues** operate on the principle of First-In-First-Out (FIFO), enabling elements to be added to the rear of the queue through the enqueue operation and removed from the front of the queue through the dequeue operation. 

In the real world, queues are formed when a first-come, first-served service is provided, such as at highway toll booths.

Think of a **queue** as people standing in line in a supermarket.

The first person to stand in line is also the first who can pay and leave the supermarket. This way of organizing elements is called FIFO: First In First Out.

Basic operations we can do on a queue are:
- **Enqueue:** Adds a new element to the queue.
- **Dequeue:** Removes and returns the first (front) element from the queue.
- **Peek:** Returns the first element in the queue.
- **isEmpty:** Checks if the queue is empty.
- **Size:** Finds the number of elements in the queue.

Experiment with these basic operations in the queue animation above.

Queues can be implemented by using arrays or linked lists.

Queues can be used to implement job scheduling for an office printer, order processing for e-tickets, or to create algorithms for breadth-first search in graphs.

---
## Application
Queues are widely utilized in solving graph-related problems and managing capacity in various contexts, such as printers, where tasks are processed in the order of arrival. They are also utilized in situations where a first-come-first-serve approach is necessary.

---
## Queue Implementation using Arrays
Reasons to implement queues using arrays:
- **Memory Efficient:** Array elements do not hold the next elements address like linked list nodes do.
- **Easier to implement and understand:** Using arrays to implement queues require less code than using linked lists, and for this reason it is typically easier to understand as well.

Reasons for **not** using arrays to implement queues:
- **Fixed size:** An array occupies a fixed part of the memory. This means that it could take up more memory than needed, or if the array fills up, it cannot hold more elements. And resizing an array can be costly.
- **Shifting cost:** Dequeue causes the first element in a queue to be removed, and the other elements must be shifted to take the removed elements' place. This is inefficient and can cause problems, especially if the queue is long.
- **Alternatives:** Some programming languages have built-in data structures optimized for queue operations that are better than using arrays.

---
## Queue Implementation using Linked Lists
Reasons for using linked lists to implement queues:
- **Dynamic size:** The queue can grow and shrink dynamically, unlike with arrays.
- **No shifting:** The front element of the queue can be removed (enqueue) without having to shift other elements in the memory.

Reasons for **not** using linked lists to implement queues:
- **Extra memory:** Each queue element must contain the address to the next element (the next linked list node).
- **Readability:** The code might be harder to read and write for some because it is longer and more complex.
---
## Queues snippets
See the full code examples here: [[Queue Snippets]]