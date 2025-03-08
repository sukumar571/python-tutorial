'''
looping statements or iterative statements:-

1)for loop
2)while loop
3)nested loop

'''

'''
* for condition is used for the sequence of iterations *
for syntax:-

for i in range(condition):
  statements
'''
# for i in range(1,10):
#     print(i)

# a=[1,10,100,20,50,30,60,70]
# for i in a:
#     print(i)

# a=[1,10,100,20,50,30,60,70]
# for i in a:
#     print(i)
# else:  # if you write block also if you print particular statement
#     print("tata bye bye")

# a='sukumar'
# for i in a:
#     print(i)


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x) 
#   if x == "banana":
#     break

# Example 3:-
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x) 
'''
while condition:
  statements
  increment or decrement

'''
# i=10
# while i<15:
#   print(i)
#   i+=1

#Example 2 :-
# i=1
# while i<10:
#     print(i)
#     if i==5:
#         break
#     i+=1


#Example 3:-
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

'''
nested loops :- if you write one loop inside another loop

--> for loop inside another for loop
--> while loop inside another while loop

'''
# a=[1,2,3,4,5]
# b=['a','b','c','d','e']
# for i in a:
#     for j in b:
#         print(i,j)
        
# a=[1,2,3,4,5]
# b=[1,2,3]
# for i in a: #1
#     for j in b: #1,2,3
#         print(i+j)


'''
Jumping statements :-

1)pass :- ignore the statements 
2)brake :- terminate the loop
3)continue :- skip (current iteration)

'''