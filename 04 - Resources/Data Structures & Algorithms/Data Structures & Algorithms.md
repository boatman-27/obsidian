---
tags:
  - DSA
date: 2025-08-18T11:20:00
roadmap: https://roadmap.sh/datastructures-and-algorithms
link: https://www.w3schools.com/dsa/dsa_intro.php
---
## Overview
Data structures are fundamental components of computer science that help organize and store data efficiently. Choosing the right data structure can optimize performance and simplify problem-solving in algorithms.

**[[Data Structures]]** are specialized formats for organizing and storing data in a computer so that it can be used efficiently. They provide a means to manage large amounts of data efficiently for uses such as large databases and internet indexing services. 
They are critical to programming and are used in almost all software systems including web development, operating systems, image editing, and much more. Some common types of **data structures** are arrays, linked lists, queues, stacks, trees, and graphs. 

The choice of the **data structure** often begins from the choice of an abstract data type, a broad type encapsulating various possible data structures.

---
## What are Data Structures?
A data structure is a way to store data.

We structure data in different ways depending on what data we have, and what we want to do with it.

First, let's consider an example without computers in mind, just to get the idea.

If we want to store data about people we are related to, we use a family tree as the data structure. We choose a family tree as the data structure because we have information about people we are related to and how they are related, and we want an overview so that we can easily find a specific family member, several generations back.

With such a family tree data structure visually in front of you, it is easy to see, for example, who my mother's mother is—it is 'Emma,' right? But without the links from child to parents that this data structure provides, it would be difficult to determine how the individuals are related.

**Data structures** give us the possibility to manage large amounts of data efficiently for uses such as large databases and internet indexing services.

**Data structures** are essential ingredients in creating fast and powerful algorithms. They help in managing and organizing data, reduce complexity, and increase efficiency.

### In Computer Science there are two different kinds of data structures:
- **Primitive Data Structures** are basic data structures provided by programming languages to represent single values, such as integers, floating-point numbers, characters, and booleans.
- **Abstract Data Structures** are higher-level data structures that are built using primitive data types and provide more complex and specialized operations. Some common examples of abstract data structures include arrays, linked lists, stacks, queues, trees, and graphs.
## What are Algorithms?
An **algorithm** is a set of step-by-step instructions to solve a given problem or achieve a specific goal.

A cooking recipe written on a piece of paper is an example of an algorithm, where the goal is to make a certain dinner. The steps needed to make a specific dinner are described exactly.

When we talk about **algorithms** in Computer Science, the step-by-step instructions are written in a programming language, and instead of food ingredients, an algorithm uses data structures.

**Algorithms** are fundamental to computer programming as they provide step-by-step instructions for executing tasks. An efficient algorithm can help us to find the solution we are looking for, and to transform a slow program into a faster one.

By studying algorithms, developers can write better programs.

Algorithm examples:
- Finding the fastest route in a GPS navigation system
- Navigating an airplane or a car (cruise control)
- Finding what users search for (search engine)
- Sorting, for example sorting movies by rating

## Data Structures together with Algorithms

**Data structures and algorithms (DSA)** go hand in hand. A data structure is not worth much if you cannot search through it or manipulate it efficiently using algorithms, and the algorithms in this tutorial are not worth much without a data structure to work on.

**DSA** is about finding efficient ways to store and retrieve data, to perform operations on data, and to solve specific problems.

By understanding **DSA**, you can:
- Decide which data structure or algorithm is best for a given situation.
- Make programs that run faster or use less memory.
- Understand how to approach complex problems and solve them in a systematic way.
## Where is Data Structures and Algorithms Needed?

**Data Structures and Algorithms (DSA)** are used in virtually every software system, from operating systems to web applications:
- For managing large amounts of data, such as in a social network or a search engine.
- For scheduling tasks, to decide which task a computer should do first.
- For planning routes, like in a GPS system to find the shortest path from A to B.
- For optimizing processes, such as arranging tasks so they can be completed as quickly as possible.
- For solving complex problems: From finding the best way to pack a truck to making a computer 'learn' from data.

**DSA** is fundamental in nearly every part of the software world:
- Operating Systems
- Database Systems
- Web Applications
- Machine Learning
- Video Games
- Cryptographic Systems
- Data Analysis
- Search Engines
---
## Theory and Terminology

| Term               | Description                                                                                                                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Algorithm          | A set of step-by-step instructions to solve a specific problem.                                                                                                                                                          |
| Data Structure     | A way of organizing data so it can be used efficiently. Common data structures include arrays, linked lists, and binary trees.                                                                                           |
| Time Complexity    | A measure of the amount of time an algorithm takes to run, depending on the amount of data the algorithm is working on.                                                                                                  |
| Space Complexity   | A measure of the amount of memory an algorithm uses, depending on the amount of data the algorithm is working on.                                                                                                        |
| Big O Notation     | A mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. Used in this tutorial to describe the time complexity of an algorithm.        |
| Recursion          | A programming technique where a function calls itself.                                                                                                                                                                   |
| Divide and Conquer | A method of solving complex problems by breaking them into smaller, more manageable sub-problems, solving the sub-problems, and combining the solutions. Recursion is often used when using this method in an algorithm. |
| Brute Force        | A simple and straight forward way an algorithm can work by simply trying all possible solutions and then choosing the best one.                                                                                          |

---
***[[Algorithmic Complexity]]*** refers to the computing resources needed by an algorithm to solve a problem. These computing resources can be the time taken for program execution (*time complexity*), or the space used in memory during its execution (*space complexity*).

---
***[[Search Algorithms]]*** are techniques used for finding a specific item or group of items among a collection of data. The primary types of search algorithms are linear search, binary search, depth-first search, and breadth-first search.

---
***[[Sorting Algorithms]]*** are used to rearrange a given array or list elements according to a comparison operator on the elements. The comparison operator is used to decide the new order of element in the respective data structure.

---
## LeetCode Problems I attempted
[[1. Two Sum]]
[[2. Add Two Numbers]]
[[20. Valid Parentheses]]
[[21. Merge Two Sorted Lists]]
[[49. Group Anagrams]]
[[88. Merge Sorted Array]]
[[141. Linked List Cycle]]
[[206. Reverse Linked List]]
[[217. Contains Duplicate]]
[[242. Valid Anagram]]
[[347. Top K Frequent Elements]]
[[704. Binary Search]]