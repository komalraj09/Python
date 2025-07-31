# 1. Write a python program to swap two numbers without using third variable.
# 2. Write a python program to swap two numbers using third variable.
# 3. Add two lists using arithmetic operator.
# 4. Find total and percentage of marks of 5 different subjects.
# 5. Find Area of circle of any given radius by the user.
# 6. Find square and cube of given number.

#1
# a = 10
# b = 50
# a = a + b
# b = a-b
# a = a-b
# print(a)
# print(b)

#2
# a = 10
# b = 20

# c = a
# a = b
# b = c

# print(c)
# print(a)
# print(b)

#3
# list_1 = [1,2,3,4,5]
# list_2 = [3,4,5,6]

# result = list_1 + list_2

# print(result)

# #4

# sub_1 = 80
# sub_2 = 75
# sub_3 = 85
# sub_4 = 89
# sub_5 = 95

# total = sub_1 + sub_2 + sub_3 + sub_4 + sub_5
# percentage = (total / 500) * 100

# print(f"Total Marks = {total}")
# print(f"Percentage = {percentage}")

#5. Find Area of circle of any given radius by the user.

# r = float (input("Enter radius (r): "))
# area = 3.14 * r **2

# print(f"Area of circle of {r} is : {area}")

#6  Find square and cube of given number.

num = float(input("Enter number : "))

square = num ** 2
cube = num ** 3 

print(f"Square of {num} is {square} ")
print(f"cube of {num} is {cube} ")