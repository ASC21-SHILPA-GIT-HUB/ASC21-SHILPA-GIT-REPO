#string
s="Hello, World!"
print(s)
print(s.upper())
print(s.lower())
print(s.replace("World", "Python"))
print(s.split(","))
print(s.strip())
#list
l=[1,2,3,4,5]
print(l)
l.append(6)
print(l)
l.remove(3)
print(l)
print(sum(l))
#list comprehension
squares=[x**2 for x in range(1,11)]
print(squares)
ls=[2,6,4,7,9,8,1]
ls.sort()
print(ls)
ls.reverse()
print(ls)
lst=ls.copy()
print(lst)
#dictionary
d={"name":"Alice","age":30,"city":"New York"}
print(d)
dic = {
   101:{"name": "wireless mouse", "price": 25.99, "quantity": 2},
    102:{"name": "keyboard", "price": 45.50, "quantity": 1},
    103:{"name": "USB-C cable", "price": 10.00, "quantity": 3}
}
print(dic)
print(dic[101]["name"])
print(dic[102]["price"])
dic[103]["quantity"]=5
print(dic[103]["quantity"])
