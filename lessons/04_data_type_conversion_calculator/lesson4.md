# 🧮 Lesson 4: Data Type Conversion & Practice (Calculator)

In this lesson, we’ll build a **simple calculator** to practice Python’s data types and conversions.  
By the end, you’ll understand how to take input from a user, convert it to numbers, and perform real mathematical operations.

---

## 🚀 Step 1: Create a New File

1. Open your project folder in PyCharm.  
2. Create a new Python file named: lesson4_calculator.py

## 🧠 Step 2: The Simple Calculator Project

The goal is to:
- Ask the user for **two numbers**.
- Add them together.
- Display the **sum** on the screen.

Even though this seems “ridiculously simple,” it’s a perfect example of why **data type conversion** matters.

---

## 🧾 Step 3: Capturing User Input (`input()` Function)

Python’s built-in `input()` function lets your program accept information from the user.

```python
number_A = input("Enter first number: ")
number_B = input("Enter second number: ")

print(number_A + number_B)
```
>⚠️ Important: The input() function always returns text (a string) — even if the user types a number.

So, if you type 2 and 3, the output will be:

23

That’s string concatenation, not addition.

## 🔄 Step 4: Why We Need Data Type Conversion

To perform real math, we must convert the input strings into numeric types (int or float).

Example 1: Using int() for Whole Numbers
number_A = int(input("Enter first number: "))
number_B = int(input("Enter second number: "))

print(number_A + number_B)


✅ Output:

Enter first number: 2
Enter second number: 3
5

Example 2: When the User Enters Decimals

If a user types 2.5 instead of 2, you’ll get an error:

ValueError: invalid literal for int() with base 10: '2.5'


That’s because int() can only handle whole numbers.

Example 3: Using float() for Decimal Numbers
number_A = float(input("Enter first number: "))
number_B = float(input("Enter second number: "))

print(number_A + number_B)


✅ Output:

Enter first number: 2.5
Enter second number: 3.5
6.0


> 💡 Use int() for whole numbers and float() for decimals.

## 🧰 Step 5: Other Conversion Functions

Python provides many conversion functions, but they only work if the data makes sense.

| Function | Converts To | Example                               | Valid? |
| :--- | :--- |:--------------------------------------| :--- |
| int() | Integer | `int("5")` $\to$ 5                    | ✅ |
| float() | Decimal number | `float("3.14")` $\to 3.14$            | ✅ |
| str() | String | `str(10)` $\to$ 10                    | ✅ |
| bool() | Boolean | `bool("")` $\to$ `False`              | ✅ |
| list() | List | `list("abc")` $\to$ `['a', 'b', 'c']` | ✅ |
| int("hello") | ❌ Invalid | Raises `ValueError`                   | ❌ |

⚠️ If you try to convert something that doesn’t logically fit (like "hello" → int), Python will throw an error.

## 🧩 Step 6: Practice Challenge

Create a Python file called lesson4_practice.py and follow these steps:

Ask the user for two inputs.

Convert them to floats.

Add the two numbers together.

Print the result using an f-string.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}")


✅ Example Output:

Enter first number: 5
Enter second number: 10
The sum of 5.0 and 10.0 is 15.0

## 🧭 Lesson Summary

input() always returns text — even if the user enters numbers.

Use data type conversion functions (int(), float()) to perform calculations.

Invalid conversions (like "hello" → int) cause ValueError.

Always test and experiment — errors are part of learning.

🏁 Next Lesson: We’ll explore collection data types like lists, tuples, and sets — the foundations of data organization in Python.