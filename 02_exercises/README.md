# 02_exercises

Hands-on code backing each chapter. See each `partN/README.md` for that part's exercise template.

## `# LEARN:` comments

Code in this folder is teaching material, for Bruno and for readers who may be newer to Python than the manuscript's target reader. Where a script does something worth explaining (why a pattern is used, why something is a problem, what a stdlib function does), add a comment tagged `# LEARN:` rather than a normal comment.

This keeps two kinds of comments distinct:
- Normal comments: notes that belong in the code regardless of audience (a non-obvious constraint, a workaround).
- `# LEARN:` comments: explanatory, for someone learning Python or the concept, not required for the code itself to make sense to an experienced engineer.

Tagging them makes it easy to find and strip later if a script should read as production code rather than a tutorial: `grep -rn "# LEARN:" 02_exercises/` to find them all, or a one-line script to strip them if the teaching comments are no longer wanted.
