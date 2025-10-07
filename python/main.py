storename= "shopease"
welcome = f"welcome to {storename}!"
print(welcome)

#different variables in python
item_count= 5
item_price= 20.5
is_available= True
discount= None
item_list= ["apple", "banana", "orange"]
item_tuple= ("apple", "banana", "orange")
item_set= {"apple", "banana", "orange"}
item_dict= {"name": "apple", "price": 20.5, "quantity": 5}

#printing the variables and their types
print(item_count, type(item_count))
print(item_price, type(item_price))
print(is_available, type(is_available))
print(discount, type(discount))
print(item_list, type(item_list))
print(item_tuple, type(item_tuple))
print(item_set, type(item_set))
print(item_dict, type(item_dict))

#type conversion
item_count_str= str(item_count)
item_price_int= int(item_price)
item_price_float= float(item_price)
print(item_count_str, type(item_count_str))
print(item_price_int, type(item_price_int))
print(item_price_float, type(item_price_float))


