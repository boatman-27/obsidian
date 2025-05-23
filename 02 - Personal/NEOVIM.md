		# Most Important Vim Motions

This cheat sheet lists essential Vim motions, which are used to move the cursor and can be combined with operators like `d`, `y`, or `c`.

---

## Cursor Movement

| Motion | Description                                                |
| ------ | ---------------------------------------------------------- |
| `h`    | Left                                                       |
| `l`    | Right                                                      |
| `k`    | Up                                                         |
| `j`    | Down                                                       |
| `gj`   | Moves down by screen line                                  |
| `gk`   | Moves Up by screen line                                    |
| `H`    | Top of the screen                                          |
| `M`    | Middle of the screen                                       |
| `L`    | Bottom of the screen                                       |
| `w`    | Jumps forward to the start of the next word a word         |
| `W`    | Jumps forward to the start of a word after a space         |
| `e`    | Jumps forward to the end of the next word                  |
| `E`    | Jumps forward to the end of the next word after a space    |
| `b`    | Jumps backward to the start of a word                      |
| `B`    | Jumps backward to the start of the next word after a space |


---

## Word Motions

| Motion | Description                          |
|--------|--------------------------------------|
| `w`    | Start of next word                   |
| `W`    | Start of next WORD (non-punctuation) |
| `e`    | End of current/next word             |
| `E`    | End of current/next WORD             |
| `b`    | Start of previous word               |
| `B`    | Start of previous WORD               |

---

## Line Motions

| Motion | Description             |
|--------|-------------------------|
| `0`    | Beginning of line       |
| `^`    | First non-blank char    |
| `$`    | End of line             |
| `g_`   | Last non-blank char     |

---

## Sentence and Paragraph Motions

| Motion | Description         |
|--------|---------------------|
| `)`    | Next sentence       |
| `(`    | Previous sentence   |
| `{`    | Beginning of paragraph |
| `}`    | End of paragraph     |

---

## Screen Motions

| Motion | Description                        |
|--------|------------------------------------|
| `H`    | Top of screen                      |
| `M`    | Middle of screen                   |
| `L`    | Bottom of screen                   |
| `zz`   | Center line on screen              |
| `zt`   | Move line to top of screen         |
| `zb`   | Move line to bottom of screen      |

---

## Search Motions

| Motion | Description                    |
|--------|--------------------------------|
| `/word` | Search forward for "word"     |
| `?word` | Search backward for "word"    |
| `n`     | Repeat last search            |
| `N`     | Repeat in opposite direction  |

---

## Paragraph/Text Object Motions

| Motion | Description                      |
|--------|----------------------------------|
| `aw`   | A word (includes space)         |
| `iw`   | Inner word                      |
| `ap`   | A paragraph                     |
| `ip`   | Inner paragraph                 |
| `a"`   | A quoted string                 |
| `i"`   | Inside quoted string            |

---

## Line Number Motions

| Motion | Description              |
|--------|--------------------------|
| `G`    | Go to last line          |
| `gg`   | Go to first line         |
| `:n`   | Go to line `n`           |
| `{n}G` | Go to line `n`           |

---

## Marks and Jumps

| Motion | Description                        |
|--------|------------------------------------|
| `'a`   | Go to line of mark `a`             |
| `` `a `` | Go to exact position of mark `a` |
| `''`   | Go to last jump location           |
| `Ctrl-o` | Older cursor position (back)     |
| `Ctrl-i` | Newer cursor position (forward)  |

---

## Folding & Other Useful Motions

| Motion | Description               |
|--------|---------------------------|
| `%`    | Jump to matching bracket  |
| `[[`   | Previous function start   |
| `]]`   | Next function start       |

---

## Tips

- Combine motions with operators:  
  - `d` (delete), `y` (yank), `c` (change), `v` (visual)
  - Example: `dw` deletes the word under the cursor.

