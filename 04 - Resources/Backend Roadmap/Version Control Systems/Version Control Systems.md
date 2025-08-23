---
tags:
  - backend
date: 2025-07-20T14:22:00
---
Version control, also known as source control, is the practice of tracking and managing changes to software code. Version control systems are software tools that help software teams manage changes to source code over time.

Version control software keeps track of every modification to the code in a special kind of database. If a mistake is made, developers can turn back the clock and compare earlier versions of the code to help fix the mistake while minimizing disruption to all team members.

Software developers working in teams are continually writing new source code and changing existing source code. The code for a project, app or software component is typically organized in a folder structure or "file tree".

By far, the most widely used modern version control system in the world today is Git. Git is a mature, actively maintained open source project originally developed in 2005 by Linus Torvalds, the famous creator of the Linux operating system kernel.

Having a distributed architecture, Git is an example of a DVCS (hence Distributed Version Control System). Rather than have only one single place for the full version history of the software as is common in once-popular version control systems like CVS or Subversion (also known as SVN), in Git, every developer's working copy of the code is also a repository that can contain the full history of all changes.

In addition to being distributed, Git has been designed with performance, security and flexibility in mind.

### Performance
Committing new changes, branching, merging and comparing past versions are all optimized for performance. The algorithms implemented inside Git take advantage of deep knowledge about common attributes of real source code file trees, how they are usually modified over time and what the access patterns are.

Unlike some version control software, Git is not fooled by the names of the files when determining what the storage and version history of the file tree should be, instead, Git focuses on the file content itself. After all, source code files are frequently renamed, split, and rearranged. The object format of Git's repository files uses a combination of delta encoding (storing content differences), compression and explicitly stores directory contents and version metadata objects.

### Security
Git has been designed with the integrity of managed source code as a top priority. The content of the files as well as the true relationships between files and directories, versions, tags and commits, all of these objects in the Git repository are secured with a cryptographically secure hashing algorithm called SHA1. This protects the code and the change history against both accidental and malicious change and ensures that the history is fully traceable.

### Flexibility
One of Git's key design objectives is flexibility. Git is flexible in several respects: in support for various kinds of nonlinear development workflows, in its efficiency in both small and large projects and in its compatibility with many existing systems and protocols.

Git has been designed to support branching and tagging as first-class citizens (unlike SVN) and operations that affect branches and tags (such as merging or reverting) are also stored as part of the change history. Not all version control systems feature this level of tracking.

---
## Setting up a repository: `git init`

A [Git repository](https://bitbucket.org/product/code-repository) is a virtual storage of your project. It allows you to save versions of your code, which you can access when needed.

The [[`git init`]] command creates a new Git repository. It can be used to convert an existing, unversioned project to a Git repository or initialize a new, empty repository.

Executing `git init` creates a `.git` subdirectory in the current working directory, which contains all of the necessary Git metadata for the new repository. This metadata includes subdirectories for objects, refs, and template files. A `HEAD` file is also created which points to the currently checked out commit.

Initialize an empty Git repository, but omit the working directory. Shared repositories should always be created with the `--bare` flag. 

The `--bare` flag creates a repository that doesn’t have a working directory, making it impossible to edit files and commit changes in that repository. You would create a bare repository to git push and [[`git pull`]] from, but never directly commit to it. Central repositories should always be created as bare repositories because pushing branches to a non-bare repository has the potential to overwrite changes. 

Think of `--bare` as a way to mark a repository as a storage facility, as opposed to a development environment. This means that for virtually all Git workflows, the central repository is bare, and developers local repositories are non-bare.

---
## Cloning an existing repository: `git clone`

If a project has already been set up in a central repository, the clone command is the most common way for users to obtain a local development clone. Like `git init`, cloning is generally a one-time operation.

```bash
git clone <repo url>
```

[[`git clone`]] a repository URL. Git supports a few different network protocols and corresponding URL formats. In this example, we'll be using the Git SSH protocol. Git SSH URLs follow a template of: `git@HOSTNAME:USERNAME/REPONAME.git`

An example Git SSH URL would be: `git@bitbucket.org:rhyolight/javascript-data-store.git` where the template values match:

- `HOSTNAME: bitbucket.org`
- `USERNAME: rhyolight`
- `REPONAME: javascript-data-store`

When executed, the latest version of the remote repo files on the main branch will be pulled down and added to a new folder. The new folder will be named after the REPONAME in this case `javascript-data-store`. The folder will contain the full history of the remote repository and a newly created main branch.

---
## Saving changes to the repository: `git add` and `git commit`

he traditional software expression of "saving" is synonymous with the Git term "committing". A commit is the Git equivalent of a "save". Traditional saving should be thought of as a file system operation that is used to overwrite an existing file or write a new file. Alternatively, Git committing is an operation that acts upon a collection of files and directories.

The [[`git add`]] command adds a change in the working directory to the staging area. It tells Git that you want to include updates to a particular file in the next commit. However, `git add` doesn't really affect the repository in any significant way—changes are not actually recorded until you run [[`git commit`]].

### Common options
---

```bash
git add <file>
```

Stage all changes in `<file>` for the next commit.

```bash
git add <directory>
```

Stage all changes in `<directory>` for the next commit.

```bash
git add -p
```

Begin an interactive staging session that lets you choose portions of a file to add to the next commit. This will present you with a chunk of changes and prompt you for a command. Use `y` to stage the chunk, `n` to ignore the chunk, `s` to split it into smaller chunks, `e` to manually edit the chunk, and `q` to exit.

```bash
git add . 
```

stages all changes in the entire project directory.

```bash
git commit
```

Commit the staged snapshot. This will launch a text editor prompting you for a commit message. After you’ve entered a message, save the file and close the editor to create the actual commit.

```bash
git commit -a
```

Commit a snapshot of all changes in the working directory. This only includes modifications to tracked files (those that have been added with `git add` at some point in their history).

```bash
git commit -m "commit message"
```

A shortcut command that immediately creates a commit with a passed commit message. By default, `git commit` will open up the locally configured text editor, and prompt for a commit message to be entered. Passing the `-m` option will forgo the text editor prompt in-favor of an inline message.

```bash
git commit -am "commit message"
```

A power user shortcut command that combines the `-a` and `-m` options. This combination immediately creates a commit of all the staged changes and takes an inline commit message.

```bash
git commit --amend
```

This option adds another level of functionality to the commit command. Passing this option will modify the last commit. Instead of creating a new commit, staged changes will be added to the previous commit. This command will open up the system's configured text editor and prompt to change the previously specified commit message.

---
## Repo-to-repo collaboration: `git push`

The [[`git push`]] command is used to upload local commits to a remote repository. It updates the remote branch with the commits you have made locally.

### Basic Syntax
```bash
git push <remote> <branch>
```
- `<remote>`: Usually `origin` (the default name for your remote).
- `<branch>`: The branch you want to push (e.g., `main`, `master`, `dev`).

### Common Examples
#### Push current branch to `origin`
```bash
git push origin main
```
Pushes the local `main` branch to the remote `origin`.
#### Push all branches
```bash
git push --all origin
```
Pushes all local branches to the remote.
#### Push tags
```bash
git push --tags
```
Pushes all local tags to the remote.

---
## Inspecting a repository `git status` and `git log`

The `git status` command displays the state of the working directory and the staging area. It lets you see which changes have been staged, which haven’t, and which files aren’t being tracked by Git. Status output does _not_ show you any information regarding the committed project history. For this, you need to use [`git log`](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-log).

The `git status` command is a relatively straightforward command. It simply shows you what's been going on with `git add` and `git commit`. Status messages also include relevant instructions for staging/unstaging files. Sample output below:

```bash
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .DS_Store
        modified:   Backend/.DS_Store

no changes added to commit (use "git add" and/or "git commit -a")
```

The `git log` command displays committed snapshots. It lets you list the project history, filter it, and search for specific changes. While `git status` lets you inspect the working directory and the staging area, `git log` only operates on the committed history. Sample output below:
```bash
commit f99893484ee881672e2f0283eec3c12050d4b083 (HEAD -> master, origin/master)
Author: Adham <adham4603@gmail.com>
Date:   Fri Jul 18 11:41:26 2025 +0400

    Refactor: return pointers in user functions and update documentation

    Updated all relevant functions in the user handler to return pointer types for consistency and extensibility. Also revised function docstrings to reflect changes in return types and parameter expectations.

commit d60f5bb32f0716767cbd1e0aa0ced5a0e9613b88
Author: Adham <adham4603@gmail.com>
Date:   Thu Jul 3 12:32:50 2025 +0400

    added readme

commit 6b1f50b87f9fd6dbeec3712f1408a7cad13390be
Author: Adham <adham4603@gmail.com>
Date:   Thu Jul 3 12:31:14 2025 +0400

    added readme

commit f6e80f94422b4bff96cce4e8ea7dbe1dd1afd486
Author: Adham <adham4603@gmail.com>
Date:   Thu Jul 3 11:58:38 2025 +0400

    first commit
```
### Usage

```bash
git log
```

Display the entire commit history using the default formatting. If the output takes up more than one screen, you can use `Space` to scroll and `q` to exit.

```bash
git log -n <limit>
```

Limit the number of commits by . For example, `git log -n 3` will display only 3 commits.

Condense each commit to a single line. This is useful for getting a high-level overview of the project history.

```bash
git log --oneline
```

```bash
git log --stat
```

Along with the ordinary `git log` information, include which files were altered and the relative number of lines that were added or deleted from each of them.

```bash
git log -p
```

Display the patch representing each commit. This shows the full diff of each commit, which is the most detailed view you can have of your project history.

```bash
git log --author="<pattern>"
```

Search for commits by a particular author. The `＜pattern＞` argument can be a plain string or a regular expression.

```bash
git log --grep="<pattern>"
```

Search for commits with a commit message that matches `＜pattern＞`, which can be a plain string or a regular expression.

---
You can create a [[`.gitignore`]] file in your repository's root directory to tell Git which files and directories to ignore when you make a commit. To share the ignore rules with other users who clone the repository, commit the `.gitignore` file in to your repository.

---
## Fetching and pulling from Git remotes
---

Once a remote record has been configured through the use of the `git remote` command, the remote name can be passed as an argument to other Git commands to communicate with the remote repo. Both [git fetch](https://www.atlassian.com/git/tutorials/syncing/git-fetch), and [git pull](https://www.atlassian.com/git/tutorials/syncing/git-pull) can be used to read from a remote repository. Both commands have different operations that are explained in further depth on their respective links.

---
## Github
### About GitHub
GitHub is a cloud-based platform where you can store, share, and work together with others to write code.

Storing your code in a "repository" on GitHub allows you to:

- **Showcase or share** your work.
- **Track and manage** changes to your code over time.
- Let others **review** your code, and make suggestions to improve it.
- **Collaborate** on a shared project, without worrying that your changes will impact the work of your collaborators before you're ready to integrate them.

Collaborative working, one of GitHub’s fundamental features, is made possible by the open-source software, Git, upon which GitHub is built. [[Git Branching]]
