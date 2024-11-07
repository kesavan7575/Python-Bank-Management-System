from num2words import num2words
 

a='hello hello kesavan 123'
b=a.split()
c=list(set(b))
d=" ".join(c)
e=d.title()
print(e)