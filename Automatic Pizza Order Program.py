#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Welcome to Python Pizza Deliveries!")
size = input("What size Pizza do you want? S, M or L ").lower()
pepperoni = input("Do you want Pepperoni? Y or N ").lower()
cheese = input("Do you want cheese? Y or N ").lower()
price = 0
if size == 's':
    price += 15
elif size == 'm':
    price += 20
elif size == 'l':
    price += 25
else:
    print("Wrong pizza size")
if pepperoni == 'y' and size == 's':
    price += 2
elif pepperoni == 'y':
    price += 3
else:
    price+=0
if cheese == 'y':
    price +=1
else:
    price+=0
print(f"Your final bill is ${price}. ")


# In[ ]:




