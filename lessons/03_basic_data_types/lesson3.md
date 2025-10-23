# 🐍 Lesson 3: Basic Data Types

In this lesson, we’ll explore the **five fundamental data types** in Python and how to work with them. Understanding data types is crucial for performing operations, storing information, and building programs.

---

## 🧩 Step 1: Create a New Python File
1. Open your code editor.
2. Create a new file named: lesson3_basic_data_types.py


---

## 🧠 Step 2: Core Data Types in Python

| Data Type       | Description                                   | Syntax / Example                  |
|-----------------|-----------------------------------------------|----------------------------------|
| **String (str)** | Used for text data. Must be in quotes.       | `"Hello"` or `'Hello'`           |
| **Integer (int)** | Whole numbers, without decimals.            | `10`, `5`, `100`                 |
| **Float (float)** | Numbers with decimals.                      | `3.14`, `34.1`                    |
| **Boolean (bool)** | Logical values, True or False.             | `True`, `False`                   |
| **NoneType (None)** | Represents no value or absence of data.   | `None`                            |

---

## ⚙️ Step 3: Checking Data Types
Python allows you to **check the type of a variable** using the `type()` function.  

```python
name = "Alice"
age = 25
is_student = True
nothing = None

print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(is_student)) # <class 'bool'>
print(type(nothing))    # <class 'NoneType'>
```
> 💡 Tip: Nest type() inside print() to see the output in the console.

## ✨ Step 4: Using f-Strings for Dynamic Text

f-Strings (formatted string literals) allow you to include variables directly inside strings:
```python
name = "Alice"
age = 25

print(f"My name is {name} and I am {age} years old.")
```

Output:
> My name is Alice and I am 25 years old.

✅ Using f-strings is the modern, cleanest way to combine text and variables.

## 🧩 Step 5: Mini Practice Exercise

- Create a Python file named lesson3_practice.py and try the following:

- Define 3–4 variables (e.g., name, age, city, hobby).

- Print the data type of each variable to confirm.

- Write a short paragraph about yourself using these variables.

- Use f-strings to include the variables dynamically in the paragraph.

Example:

name = "Maleek"
age = 99
city = "Paris"
hobby = "coding"

print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>

print(f"Hi, my name is {name}. I am {age} years old, live in {city}, and enjoy {hobby}.")

## 🧭 Lesson Summary

Python has 5 fundamental data types: str, int, float, bool, NoneType.

Use type() to check a variable’s type.

f-Strings allow easy integration of variables into text.

Storing values in variables ensures reuse and efficiency.

🏁 Next Lesson: We’ll apply this knowledge to [data type conversion](../04_data_type_conversion_calculator/lesson4.md) and build a simple calculator.