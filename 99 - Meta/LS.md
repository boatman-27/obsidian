# Go-LS: A Colorful, Git-Aware Directory Listing Tool

Go-LS is a simple command-line utility written in Go that mimics the behavior of the Unix `ls` command with some handy enhancements:

- Displays directory contents with file sizes and last modification times.
- Colorizes output: directories, symlinks, and files are visually distinct.
- Detects and displays symbolic link targets.
- Shows Git repository info (current branch, upstream, latest commit) if inside a Git repo.
- Supports sorting by name, size, or modification time.
- Uses a neat, human-readable time format like "just now", "5 mins ago", or "2 months ago".
- Displays a summary of total files, directories, and total bytes.
- **File icons:** file and folder icons are adapted from the [eza](https://github.com/eza-community/eza) project.
---

## Features

- **Colorized output:** directories (blue), symlinks (yellow), normal files (default).
- **Git integration:** displays local branch, remote tracking branch, and latest commit hash.
- **Sorting:** sort the directory listing by `name`, `size`, or `modtime`.
- **Symlink resolution:** shows the target of symlinks (or marks broken links).
- **Human-friendly modification timestamps.**
- **File size displayed in bytes.**

---
## Installation

Make sure you have [Go](https://golang.org/dl/) installed (version 1.16+ recommended).
Clone the repository and build:

```bash
git clone https://github.com/yourusername/go-ls.git
cd go-ls
go build -o gols
```
---
## Usage

Run the binary from your terminal:
```bash
./gols [--path /some/directory] [--sort name|size|modtime]
```

- `--path`: Specify the directory to list (defaults to current directory).
- `--sort`: Specify sorting criteria (`name`, `size`, or `modtime`). Defaults to unsorted.
### Example
```bash
./gols --path ~/Developer/ --sort modtime
```
---
### Example Output
```bash
/Users/adhamosman/Developer/termPortfolio/
╭────────────────────┬────────────────────────────┬────────────────────────╮
│ LOCAL BRANCH: MAIN │ REMOTE BRANCH: ORIGIN/MAIN │ LATEST COMMIT: DFFFE42 │
│ FILE NAME          │          FILE SIZE (BYTES) │ LAST MODIFIED          │
├────────────────────┼────────────────────────────┼────────────────────────┤
│  .DS_Store        │                       6148 │       3 days ago       │
│  termPortfolio    │                        544 │       7 days ago       │
╰────────────────────┴────────────────────────────┴────────────────────────╯
 1 files,  1 dirs  Σ 6148 bytes%   
```
---
## Notes
- The icons used for files and directories are inspired by the excellent [eza](https://github.com/eza-community/eza) terminal listing tool.
- Symlinks are shown with their targets; broken symlinks are indicated.    
- The color output uses ANSI escape codes and works in most terminals.
---
## Contributing
Feel free to open issues or pull requests for enhancements or bug fixes.