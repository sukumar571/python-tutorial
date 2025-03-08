'''
tuple:-
->list is used to store multiple items in a single variable.
->list is created by using the parenthesis '()' or by using the tuple key word.
->list is ordered, immutable(unchangeable), and allow duplicate values.
->list can allow to store different types of data.
->only two methods in tuple 1)index() 2)count()
->the main difference list and tuple is mutable and immutable respectively.

'''
# t1=()
# print(type(t1))

# t1=tuple()
# print(type(t1))

# t1=(1,2,3,'suku',(3+5j),True)
# print(len(t1)) #length
# print(t1[3])   #accessing 
# print(t1[1:4]) #slicing

'''adding of the 2 tuples'''
# t1=('a','b','c')
# t2=(1,2,3)
# print(t1+t2)

# t1=(1,3,5,8,2,6,3,3,3,4,)
# print(t1.count(3))
# print(min(t1))
# print(max(t1))
# print(sum(t1))

'''checking the elements'''
# t1=(1,3,5,8,2,6,3,3,3,4,)
# print(1 in t1)
# print(1 not in t1)

'''comparing the tuples'''
# t1=(1,2,3)
# t2=(1,2,3)
# print(t1 is t2)
# print(t1 is not t2)

# t1=(1,3,5,8,2)
# print(t1*2)

'''
->tuples is immutable you can't change
->but of you want to change the tuple 
1)first if you convert the tuple into list and then
2)perform the list methods and then
3)convert the list into tuple

'''
# t1=(1,2,3)
# l1=list(t1)
# l1.append('suku')
# t1=tuple(l1)
# print(t1)

'''unpacking the elements'''

# fruits=('apple','banana','cherry')
# (green,yellow,red)=fruits
# print(green,yellow,red)

''' by using  Asterisk* '''
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry","pine apple")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry","pine apple")

# (green, *yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)