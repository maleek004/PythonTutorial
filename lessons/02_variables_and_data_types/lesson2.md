# 🐍 Lesson 2: Python Syntax, Errors, and Variables

## 🧠 1. Understanding Python Syntax
**Syntax** is the set of rules (or grammar) that Python uses to understand your code.

If your code breaks these rules, Python will display an **error message** instead of running it.  
Don’t be discouraged — **errors are your best teachers!**

> 💡 Tip: When an error message looks confusing, copy it and ask an AI assistant (like ChatGPT or Judge) to explain what it means.

### ✅ Try it yourself
1. Open your Python editor.
2. Type the line below **without quotes** (to intentionally cause an error):
   ```python
   print(Hello world)
3. Run it and read the error message.
4. Then fix it by adding quotes:
    ```python 
    print("Hello world")
## 📦 2. Variables — Containers for Data

Variables are like boxes that store information for later use.

### 🧩 How to Create a Variable

Use the assignment operator = to store data in a variable:

text = "hello"


Here,

text → the variable name

"hello" → the data stored inside it

Now you can reuse it:

print(text)

⚙️ Why Variables Matter

If you store your data in variables, you can change the value once and have it update everywhere else in your code — saving time and avoiding errors.

## 💬 3. Commenting Your Code

Comments are lines meant for humans, not Python. They help you or others understand what the code does.

To write a comment, start the line with #

# This prints a greeting
print("Hello!")


Comments can also appear after code:

print("Bye!")  # Ends the program


💡 Shortcut: Highlight multiple lines and press Ctrl + / to comment or uncomment them quickly.

### 🐍 4. Variable Naming Rules & Conventions

To make your code clean and readable:

✅ Best Practices

- Use snake_case: all lowercase, words separated by underscores.
Example: 
```python 
user_name = "Maleek"
```
- Keep names short but meaningful.
- Avoid numbers at the start of a name:
❌ 1value = 10
- Avoid special characters like @, $, %, !
- Don’t use Python keywords (like for, if, print) or built-in names (sum, list, etc.).
If you must, add an underscore:

```python 
sum_ = 100
```
## 🧵 5. String Data Type

Textual data in Python is called a string.

### ✍️ String Basics

- You can use either single or double quotes:

> 'hello' or "hello" works fine.

- You can also mix them if you need quotes inside quotes:

>'He said "Hello"'

- ⚠️ Writing text without quotes causes a syntax error:

greeting = Hello   # ❌ This will fail because python thinks Hello here is another variable 

### 🧩 Practice Challenge

Create a new Python file called lesson2_practice.py and try the following:

Create a variable called name that stores your first name.

Add a comment describing what your code does.

Print your name to the console.

Try changing the variable value and run your code again.

🧭 Lesson Summary

In this lesson, you learned:

🧱 Python syntax is like grammar — follow its rules to avoid errors.

⚠️ Errors are learning opportunities.

📦 Variables store and reuse data efficiently.

💬 Comments make your code easier to understand.

🧵 Strings are how Python handles text.

🏁 Before moving on:
Make sure you can create variables, write comments, and print text without syntax errors.
These are the building blocks for everything else you’ll learn in Python!

Next Lesson: [Basic data types](../03_basic_data_types/lesson3.md)