

1. What is Regex?
Regex=Regular Expressions
Regex is a pattern used to search and manipulate text.
For example, suppose you have:
    User admin logged in from 192.168.1.25
You could use regex to extract:
    192.168.1.25
Think of it like:
Large Text
    ↓
Regex Pattern
    ↓
Matching Data

2. Python's re Module
Python provudes the built-in re module

    import re

7. Importtant Regex Symbols
These are the symbols you should memorize.

| Pattern | Meaning              |
| ------- | -------------------- |
| `\d`    | Digit                |
| `\D`    | Not a digit          |
| `\w`    | Word character       |
| `\W`    | Not a word character |
| `\s`    | Whitespace           |
| `\S`    | Not whitespace       |
| `.`     | Any character        |
| `^`     | Start of string      |
| `$`     | End of string        |


10. Quantifiers
Quantifiers tell regex how many times something can appear.
| Quantifier | Meaning         |
| ---------- | --------------- |
| `*`        | 0 or more       |
| `+`        | 1 or more       |
| `?`        | 0 or 1          |
| `{n}`      | Exactly n       |
| `{n,m}`    | Between n and m |
