# Collections intro

Collection is a built-in Python module that implements specialized container
datatypes providing alternatives to Python's general purpose built-in 
containers such as dict , list , set , and tuple

- **Lists**
- **Tuples**
- **Dictionaries**
- **Sets** and **Frozen Sets**


### 1. Lists

Collection of data. Ordered. Mutable

```python
#making a list in python

shoppingList = ["eggs", "bread", "cheese", "haggis"]

print(shoppingList)


breadPop = shoppingList.pop(1)

print(shoppingList)

shoppingList.remove("eggs")

shoppingList.append("butter")
print(shoppingList)

print("this is my pop val: " + breadPop)


#list slicing
shoppingList = ["eggs", "bread", "cheese", "haggis"]
print(shoppingList[1:3])

print(shoppingList[::2]) #every second step skipped over
```

<br />

### 2. Tuples
Collection of data. Ordered. Immutable
```python
essentials = ("bread", "eggs", "milk")
print(essentials)

print(essentials.count("bread"))
```

<br />

### 3. Dictionaries
Key value pairs. Key is the reference, value is the content.
Mutable.

```python
student1 = {
    "name": "Jane",
    "number": "021564646",
    "grade": 11,
    "completedLessons": 4,
    "completedLessonNames": ["variables", "git", "dataTypes", "collections"]
}

print(student1["grade"])

student1["completedLessons"] = 3

student1["completedLessonNames"].remove("dataTypes")

print(student1["completedLessonNames"])

print(student1.keys())
print(student1.values())

for key, val in student1.items(): #prints the dict
    print(key + ": " + str(val))

```
<br />

### 4. Sets and Frozen Sets
Both are unordered. Frozen list is also immutable.
```python
car_parts = {"wheels", "windows", "exhaust", "steering wheel"}

print(car_parts)

#add to a set

car_parts.add("doors")
print(car_parts)

car_parts.remove("windows")

print(car_parts)


#frozen set
#imutable set
#this is so ugly
#built in function
x = frozenset(["two", "one", "three", "four"]) # a list wrapped in a frozen set

print(x)
```

