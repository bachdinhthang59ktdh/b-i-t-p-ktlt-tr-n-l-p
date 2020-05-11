a=[2,3,4,5,6,7,8,9,5]
b=[-1,2,3,-2,4,5,-6,-7]
c=a+b #Ghép a và b thành list c
print(a) # In ra list a
print(b) # In ra list b
print(c) # In ra list c
c.sort() # Sắp xếp list c tăng dần
print(c.count(7))
print(c.index(7))
c=list(set(c))
print(c)
