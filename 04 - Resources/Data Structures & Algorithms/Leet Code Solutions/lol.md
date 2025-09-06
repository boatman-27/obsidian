Given the `root` of a binary tree, return _the postorder traversal of its nodes' values_.
### **Example 1:**
```markdown
**Input:** root = [1,null,2,3]
**Output:** [3,2,1]
```
### **Example 2:**
```markdown
**Input:** root = [1,2,3,4,5,null,8,null,null,6,7,9]
**Output:** [4,6,7,5,2,9,8,3,1]
````
### **Example 3:**
```markdown
**Input:** root = []
**Output:** []
```

### **Example 4:**

**Input:** root = [1]

**Output:** [1]

**Constraints:**

- The number of the nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?