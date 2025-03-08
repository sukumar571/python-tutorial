'''
string :- string is nothing but collection of characters 
---> it is by the following ways
1)single quotes - ' '
2)double quotes - " "
3)triple quotes - ''' '''

'''
# str='python language'
# str1="python language"
# str2='''python language'''
# print(type(str))
# print(type(str1))
# print(type(str2))

'''for checking the string is present or not ex-2,3'''
#Example 2:-
# a="sukumar is a good boy"
# if "bad" in a:
#     print("yes present")
# else:
#     print("not present")

#Example 3:-
# txt="all students are good in the class"
# print("students" in txt)

#Example 4:-
# a="sukumar"   # if you calculate length index starting from 1
# print(len(a))
# print(a[3])

'''slicing the string'''
#Slice From the Start:-
# txt="geethanjali college"
# print(txt[:11])

#Slice From the end:-
# txt="geethanjali college"
# print(txt[12:])

#positive indexing:-

# txt="geethanjali college"
# print(txt[3:7])

#Negative indexing:-
# txt="geethanjali college"
# print(txt[-16:-8])   #big value at right side and small value left side


# final Example:-

# txt="amaravathi is the capital of andhra pradesh"
# print(len(txt))
# print(txt[:10])
# print(txt[11:])
# print(txt[18:25])
# print(txt[-14:-8])
# print(txt[-14:])
# print(txt[11:-15])
# print(txt[-40:11]) 

# txt="geethnajali college"
# print(txt[-10:-5])
# print(txt[5:-5])
# print(txt[-15:15])

'''string concatenation'''

# a="suku"
# b="mar"
# print(a+b)

# txt1="geethanjali"
# txt2="college"
# txt3=txt1+" "+txt2
# print(txt3)

''' 
string methods:-
1)upper()
2)lower()
3)count() -	Returns the number of times a specified value occurs in a string
4)len()
5)strip() - removing white space from starting and ending
6)lstrip()
7)rstrip()
8)replace() - replace one string with another string
9)split() - splitting the words or characters and returns the list
10)find()
11)index() -	Searches the string for a specified value and returns the position of where it was found

'''

txt="    Geethanjali engineering College    "
print(len(txt))
print(txt.upper())
print(txt.lower())
print(txt.count('e'))
print(txt.strip())
print(txt.rstrip())
print(txt.lstrip())
print(txt.replace("engineering","institute of science and technology"))
print(txt.split())
print(txt.find("College")) # index should be start from Zero
print(txt.index('engineering'))

# txt="sukumar is good boy"
# print(txt.find("good"))