'''print the given year is leaf year or not'''
# year=int(input())
# if (year%400==0 and year%100==0)or(year%4==0 and year%100!=0):
#     print("leaf year")
# else:
#     print("Not a Leaf Year")

'''print the leaf years in the given range'''
year1=int(input())
year2=int(input())
for i in range(year1,year2+1):
    if (i%400==0 and i%100==0)or(i%4==0 and i%100!=0):
        print(i)