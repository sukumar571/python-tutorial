num1=int(input())
num2=int(input())
for i in range(1,max(num1,num2)):
    if num1%i==num2%i==0:
        hcf=i
lcm=num1*num2
print(lcm)
print(hcf)