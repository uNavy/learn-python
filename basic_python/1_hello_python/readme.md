# Python Comments and Execution Guide

## Introduction
This guide explains different types of comments in Python and how to execute scripts using Jupyter Notebook cells and the terminal.

---

## Comments in Python

### Single-Line Comments
Single-line comments start with `#` and are ignored by the Python interpreter.

```python
# THIS IS A COMMENT
print("Hello,")
print("Good morning!")  # THIS IS ALSO A COMMENT
```

### Multi-Line Comments
Multi-line comments are written using triple single (`'''`) or double (`"""`) quotes.

```python
'''
THIS IS A MULTI-LINE COMMENT
print("THIS STATEMENT WON'T BE EXECUTED")
'''
```

They can also be written in a single line:

```python
'''' THIS IS A MULTI-LINE COMMENT IN A SINGLE LINE '''
```

---

## Running the Script

### Using Jupyter Notebook Cells
In Jupyter Notebook, code can be divided into executable cells using `#%%`.

```python
#%%
print("Hello World")
#%%
```

### Using the Terminal
Run the script in a terminal with the following command:

```sh
python main.py
```

---

## Summary
- Use `#` for single-line comments.
- Use `'''` or `"""` for multi-line comments.
- In Jupyter Notebook, `#%%` is used to define executable cells.
- Run Python scripts using the terminal with `python filename.py`.

Happy coding! 🚀

