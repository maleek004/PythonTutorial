# 🧠 Chapter 05 — Data Collections and Structures


**Objective:** Understand the need for collection data types to store complex data, and be able to define, manipulate, and differentiate between **Lists**, **Tuples**, **Sets**, and **Dictionaries**.

---

## I. Context and Importance

### A. Necessity of Collections
- In programming, **collection data types** allow you to store and organize multiple values — not just single strings or numbers.  
- Mastering these structures provides a **solid foundation for any programming path**, from data science to web development.

### B. Priority
- The four main collection types are:
  - **List**
  - **Tuple**
  - **Set**
  - **Dictionary**
- Among them, **Lists are the absolute champion** — you’ll work with them in a lot of Python use cases, followed by the dictionaries.

---

## II. Overview of Collection Types

| Collection | Mutable (Can Change?) | Ordered (Index-Based?) | Defining Feature |
|-------------|----------------------|------------------------|------------------|
| **List** | ✅ Yes | ✅ Yes | High flexibility and frequent use |
| **Tuple** | ❌ No | ✅ Yes | Faster for large datasets |
| **Set** | ✅ Yes | ❌ No | Stores only **unique** items |
| **Dictionary** | ✅ Yes | ✅ Yes (since Python 3.7) | Uses **Key–Value pairs** |

---


## 1. 🟩 Lists

**Syntax:**
```python
my_list = [1, 2, 3, 'a', True]
# or
my_list = list((1, 2, 3))
```
**Content:**

Lists can hold any data type, including: Strings, Integers, Floats Booleans, None ,Nested lists (i.e. lists inside lists)

**Accessing Data:**

my_list[0]      # Indexing (first item)
my_list[-1]     # Negative indexing (last item)
my_list[2:5]    # Slicing (start:end)
my_list[::2]    # Every 2nd item


⚠️ Accessing an item beyond the list range raises IndexError.

**Common Functions:**

- len(my_list)
- sorted(my_list)
- sum(numbers)
- min(numbers)
- max(numbers)
- enumerate(my_list)


**Copying:**

import copy

a = [1, 2, [3, 4]]
b = copy.copy(a)       # Shallow copy
c = copy.deepcopy(a)   # Deep copy


**Key Methods:**

#### Adding
my_list.append('new_item')
my_list.extend(['x', 'y'])
my_list.insert(2, 'inserted_item')

#### Removing
my_list.remove('x')
my_list.pop()       # Removes last item
my_list.clear()

#### Organizing
my_list.sort()
my_list.reverse()
reversed_list = my_list[::-1]

#### Utility
my_list.count('apple')
my_list.index('apple')

#### Replacement
my_list[0] = 'updated_value'


#### Membership:

'maleek' in name_list
'maleek' not in name_list


#### Nested Lists Example:

daily_sales = [
    ['monday', 1, 200],
    ['tuesday', 3, 200],
    ['wednesday', 6, 200]
]


#### Looping Example:


```python
import math
for day in daily_sales:
    print(f'total revenue for {day[0]} is {math.prod(day[1:])}')
```

## 2. 🟦 Tuples

Syntax:
```python
my_tuple = (1, 2, 3)
# or
my_tuple = tuple([1, 2, 3])
```


#### Characteristics:

Immutable — cannot be changed after creation.

Faster than lists (useful for large or constant data like coordinates).

#### Functions:

- len(my_tuple)
- min(my_tuple)
- max(my_tuple)
- sum(my_tuple)
- sorted_tuple = tuple(sorted(my_tuple))
> ⚠️ when you use the sorted() function on a tuple , it will return a sorted list !! you should do this instead my_tuple = tuple(sorted(my_tuple))


#### Methods Available:
count() and index() only.

## 3. 🟨 Sets

#### Syntax:
```python
my_set = {1, 2, 3}
empty_set = set()
```
#### Characteristics:

Stores only unique items.

Unordered — no indexing or predictable order.

Great for removing duplicates.

#### Set Methods:

my_set.add(4)
my_set.discard(3)   # No error if item not found
my_set.remove(2)
my_set.pop()
my_set.clear()


#### Set's Comparison Operations:
a = {1, 2, 3}

b = {3, 4, 5}

- a.union(b)
- a.intersection(b)
- a.difference(b)
- a.symmetric_difference(b)
- a.issubset(b)
- a.issuperset(b)

## 4. 🟥 Dictionaries

#### Definition:

student = {
    "name": "Maleek",
    "age": 50,
    "course": "Python"
}


#### Key Traits:

- Key-Value Mapping 
- Mutable 
- Ordered (since Python 3.7)

#### Accessing Data:
```python

student["name"]          # 'Maleek'
student.get("email")     # None (avoids KeyError)
```

> ⚠️ Accessing a missing key raises a KeyError. Use .get() or .setdefault() to handle safely.

#### Adding and Updating:

```
student["email"] = "maleek@example.com"
student.update({"age": 26})
```

#### Removing:
```python
student.pop("course")
student.clear()
```


#### Inspecting Keys & Values:
```python
student.keys()
student.values()
student.items()
```

## 🧪 Mini Exercise — Practicing Collections (Step-by-step)

**Objective:** Practice creating and manipulating **Lists**, **Tuples**, **Sets**, and **Dictionaries**. Save your work in seperate files named `my_grocery_list.py`, 'my_backpack_weight.py' , ' '.

---

### 🔧 Setup
1. Create a new file in your project: `lesson5_practice.py`
2. 2. Open the file in your editor and run it often while you code.

---

### 📝 Task 1 — Grocery List (Lists)
**Goal:** Tell a story by creating and manipulating a grocery list.

Steps:
1. Create a list called `grocery` with at least 6 items (strings).  
```python
grocery = ["item1", "item2", "item3", "item4", "item5", "item6"]
```
2. Print a statement that you have created your grocery list and states the length of the list using len(). 
3. Add a new item eg: "butter" to the end using .append(). and print a statement about adding the item to your grocery list 
4. Insert another eg: "sugar" at index 2 using .insert(). and print a statement about inserting a new item as the third item on your list 
5. Remove "onion" using .remove(). and print a statement that says you are removing that item from your list because you no longer need it 
6. Print the list slice of the first 3 items (grocery[:3]) in a statement that these are your top priority items 
7. Reverse the list using slicing ([::-1]) and print a statement that says this is your grocery list ordered from the list important to the most 
8. Use enumerate() in a for loop to print each item with its index.

Verify: The printed outputs should show list length, updated list after each change, and indexed items.

