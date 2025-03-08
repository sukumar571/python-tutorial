'''checking the number prime or not'''
# num=int(input())
# count = 0
# for i in range(1,num+1):
#     if num%i==0:
#         count +=1
# if count == 2:
#   print('Prime')
# else:
#   print("not Prime")

'''print the prime number in the given range'''
# num1=int(input())
# num2=int(input())
# prime=[]
# for i in range(num1,num2+1):
#     count=0
#     if i<2:
#         continue
#     if i==2:
#         prime.append(2)
#         continue
#     for j in range(2,i):
#         if i%j==0:
            
#             count+=1
#             # break
#     if count==0:
#         prime.append(i)
# print(prime)

num1=int(input())
num2=int(input())
for i in range(num1,num2+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,end=" ")