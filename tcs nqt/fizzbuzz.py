n=int(input())
for i in range(1,n+1):
    if i%2==0 and i%3==0:
        print("fizz buzz")
    elif i%2==0:
        print("fizz")
    elif i%3==0:
        print("buzz")
    else:
        print(i)