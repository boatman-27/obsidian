## Git Branching Basics

### What is a Branch?

A **branch** in Git is a separate line of development. It lets you work on features, fixes, or experiments without affecting the main codebase.

### Common Commands

#### Create a New Branch

```bash
git branch feature-name
```

#### Switch to a Branch

```bash
git checkout feature-name
```

Or create and switch in one command:

```bash
git checkout -b feature-name
```

#### View All Branches

```bash
git branch
```

#### Merge a Branch into Another

Switch to the branch you want to merge _into_, then:

```bash
git merge feature-name
```

#### Delete a Branch

After merging:

```bash
git branch -d feature-name
```

---

## Resolving Push Issues with `git pull`

### Scenario

You try to push changes to GitHub:

```bash
git push origin main
```

But get this error:

```
! [rejected]        main -> main (fetch first)
error: failed to push some refs...
```

### Why?

The remote (GitHub) has commits you don't have locally. Git won't let you overwrite them without syncing first.

### Solution: Pull Before Pushing

1. **Pull the Latest Changes**

```bash
git pull origin main
```

If there's no conflict, Git will merge the changes automatically. Now you can push:

```bash
git push origin main
```

2. **If There Are Merge Conflicts**  
    Git will stop and tell you which files have conflicts. Open and edit the files to resolve them. Conflicts look like this:
```diff
<<<<<<< HEAD
Your local changes
=======
Incoming changes from GitHub
>>>>>>> origin/main
```

3. **Mark as Resolved**  
    After fixing the conflicts:
```bash
git add filename
```

Then commit the merge:

```bash
git commit
```

And push again:

```bash
git push origin main
```

---
## Best Practices

- Pull before you push, especially on shared branches.
- Use feature branches for new work.
- Delete branches after merging to keep your repo clean.
- Communicate with your team to avoid overlapping work.

---
## Related Commands

- `git fetch`: Download changes without merging.
- `git stash`: Temporarily save uncommitted work.
- `git log --oneline --graph`: Visualize branch history.
- `git rebase`: Alternative to merging for linear history (advanced).