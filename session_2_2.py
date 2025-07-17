# list

# cars = ["honda","bmw","mg"]
# print(cars)
# print(type(cars))

values_list = ["abc",12,12.7,True,None]
print(values_list)
print(type(values_list))

# Indexing 
new_values_list =  ["abc",12,12.7,True,None]
print(new_values_list[0])

 #python supprt negative indexing 
# print(new_values_list[-1])

# List methods

# Append method adds value to the end of the list.
# new_values_list.append ("computer") 
# new_values_list.append (23) 
# new_values_list.append([1,2,3])
# nums = [4,5,6] # we can pass variable , no need to give hard coded value
# new_values_list.append(nums)
# print(new_values_list)

#copy 
# when fuction return values then we have to handle that 

new_nums = [1,2,3,4]

nn = new_nums.copy()
new_nums.append (5)

nn_new = new_nums.copy()

print(nn)
print (nn_new)