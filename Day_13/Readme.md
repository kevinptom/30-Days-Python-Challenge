# Python List Data Type

## Introduction
A **list** in Python is a mutable, ordered collection of items. Lists can hold items of any data type, including other lists, making them a versatile data structure.

---

## Characteristics of Python Lists

- **Ordered**: Items in a list have a defined order that will not change unless explicitly altered.
- **Mutable**: Items in a list can be changed, added, or removed.
- **Heterogeneous**: A list can contain elements of different data types.
- **Dynamic**: Lists can grow or shrink as needed.

---

## Creating Lists:

          # Creating lists
          empty_list = []
          number_list = [1, 2, 3, 4]
          mixed_list = [1, "Python", 3.14, True]

          # Using the list() constructor
          constructed_list = list((1, 2, 3))
          print(constructed_list)  #output:[1, 2, 3]

## 🛑Question: Create an Empty list and insert elements into it and also practise basic list fuctions.

### For Example:
       empty_list=[]
       #for inserting elements
       empty_list.append(30)
       empty_list.append('apple')
       print(empty_list)   # Output : [30, 'apple']
       #for edit the items in the list with specified index position we use:
       empty_list[1] = 'orange'
       print(empty_list)  #output : [30, 'orange']
       










      










      
