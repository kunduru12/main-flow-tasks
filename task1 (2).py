#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Lists
print("Lists:")
my_list = [1, 2, 3, 4, 5]
print("Initial List:", my_list)

# Add element
my_list.append(6)
print("After adding 6:", my_list)

# Remove element
my_list.remove(4)
print("After removing 4:", my_list)

# Modify element
my_list[0] = 10
print("After modifying first element:", my_list)


# Dictionaries
print("\nDictionaries:")
my_dict = {"name": "John", "age": 25, "city": "New York"}
print("Initial Dictionary:", my_dict)

# Add key-value pair
my_dict["country"] = "USA"
print("After adding country:", my_dict)

# Remove key-value pair
del my_dict["age"]
print("After removing age:", my_dict)

# Modify value
my_dict["name"] = "Jane"
print("After modifying name:", my_dict)


# Sets
print("\nSets:")
my_set = {1, 2, 3, 4, 5}
print("Initial Set:", my_set)

# Add element
my_set.add(6)
print("After adding 6:", my_set)

# Remove element
my_set.remove(4)
print("After removing 4:", my_set)

# Union, intersection, and difference
set2 = {4, 5, 6, 7, 8}
print("Union:", my_set.union(set2))
print("Intersection:", my_set.intersection(set2))
print("Difference:", my_set.difference(set2))


# In[ ]:




