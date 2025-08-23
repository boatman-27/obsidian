The `git push` command is used to upload local repository content to a remote repository. Pushing is how you transfer commits from your local repository to a remote repo.

## Git push usage
---

```xml
git push <remote> <branch>
```

Push the specified branch to , along with all of the necessary commits and internal objects. This creates a local branch in the destination repository. To prevent you from overwriting commits, Git won’t let you push when it results in a non-fast-forward merge in the destination repository.

```css
git push <remote> --force
```

Same as the above command, but force the push even if it results in a non-fast-forward merge. Do not use the `--force` flag unless you’re absolutely sure you know what you’re doing.

Push all of your local branches to the specified remote.

```css
git push <remote> --tags
```

Tags are not automatically pushed when you push a branch or use the `--all` option. The `--tags` flag sends all of your local tags to the remote repository.

## Pushing to bare repositories
---

A frequently used, modern Git practice is to have a remotely hosted `--bare` repository act as a central origin repository. This origin repository is often hosted off-site with a trusted 3rd party like Bitbucket. 

Since pushing messes with the remote branch structure, It is safest and most common to push to repositories that have been created with the `--bare` flag. Bare repos don’t have a working directory so a push will not alter any in progress working directory content.

## Force pushing
---

Git prevents you from overwriting the central repository’s history by refusing push requests when they result in a non-fast-forward merge. So, if the remote history has diverged from your history, you need to pull the remote branch and merge it into your local one, then try pushing again.

The `--force` flag overrides this behavior and makes the remote repository’s branch match your local one, deleting any upstream changes that may have occurred since you last pulled. 

The only time you should ever need to force push is when you realize that the commits you just shared were not quite right and you fixed them with a `git commit --amend` or an interactive rebase. However, you must be absolutely certain that none of your teammates have pulled those commits before using the `--force` option.