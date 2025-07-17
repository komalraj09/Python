"""
1. Create a list with upto 10 items.
2. Append any 3 items at the end of the list
3. Print 3, 6, 8 items from the list.
4. Print second last item from the list using negative indexing.
5. Create a copy of the list and append 2 items in the copy.

"""
#1
num = [1,2,3,4,5,6,7,8,9,10]
print(num)

#2
num_append = [11,12,13]
num.append(num_append)
print(num)

#3
print(num[3],(num[6]),(num[8]))

#4
print(num[-2])

#5
num_copy = num.copy()
print(num_copy)


