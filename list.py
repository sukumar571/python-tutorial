'''
Lists:-
->list is used to store multiple items in a single variable.
->list is created by using the square brackets '[]' or by using the list key word.
->list is ordered, mutable(changeable), and allow duplicate values.
->list can allow to store different types of data.
->the main difference list and tuple is mutable and immutable respectively.

ordered:- indexed - starting index is '0'
changeable:- it is changed because by adding and removing the elements.
duplicate :- it allow repeated values.

'''
''' By using the square brackets '''
# a=[]  
# print(type(a))

''' By using the list keyword '''
# a=list()
# print(type(a))

# a=[1,5,8.6,15,'suku',True,(1+3j)]
# print(a)
# print(len(a))

''' accessing the list elements  and slicing the list '''
# a=[1,5,8.6,15,'suku',True,(1+3j)]
# print(a[3]) 
# print(a[1:5])
# print(a[-1])
# print(a[-6:-1])

''' checking the elements is present or not'''
# a=[1,5,8.6,15,'suku',True,(1+3j)]
# print(5 in a)

# a=[1,5,8.6,15,'suku',True,(1+3j)]
# if 5 in a:
#     print("yes present")

'''
List methods:-
1)append():- insert a single element in the last
2)extend():- insert multiple elements in the last
3)insert():- insert a single element in a particular index
4)remove():- remove the specific element - passing the element
5)pop()   :- remove the specific index element - passing the index value
6)sort()  :- sorting the elements either ascending order or descending order
7)reverse():- reversing the list elements
8)copy()  :- copy one list to another list
9)clear() :- it will delete the entire list
10)count():- it will count the no of time a value is repeated

'''

# a=[]
# a.append('suku')
# a.extend([1,5.8,True])
# a.insert(3,(3+4j))
# a.remove(5.8) # passing the element
# a.pop(2)  # passing the index value
# a.reverse()
# print(a)

#counting the repeated values
# a=[1,1,2,3,3,4,5,6,6,6]
# b=a.count(6)
# print(b)

# a=[1,10,57,2,49,9,35]
# a.sort()
# print(a)


# a=['suku','basha','nanu','priya','siri']
# a.extend(['nagoor','prudhvi'])  
# a.sort()
# print(a)

#copy method
# l1=[]
# l2=['suku','basha','nanu','priya','siri']
# l1=l2.copy()
# print(l1)

# l1.clear()
# print(l1)

''' Joining the lists'''

# first way
# l1=['a','b','c']
# l2=[1,2,3]
# l3=l1+l2
# print(l3)

#second way
# l1=['a','b','c']
# l2=[1,2,3]
# for x in l2:
#     l1.append(x)
# print(l1)

#third way
# l1=['a','b','c']
# l2=[1,2,3]
# l1.extend(l2)
# print(l1)

# l1=[1,2,3,4,5,6,7,8,9]
# print(min(l1))
# print(max(l1))
# print(sum(l1))