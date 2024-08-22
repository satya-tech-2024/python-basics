import numpy as np

my_list = [1, 2, 3, 45, 5]
my_tuple = (7, 8, 9, 10, 11)
print(my_list)

arr = np.array(my_list)
arr1 = np.array([my_list, my_tuple])
print(arr)
print(arr1)

string_arry = np.array([["Satya", "Subha", "Sunny", "Lucky"],["Josyula", "Josyula", "Josyula", "Josyula"]])
print(string_arry)

print(string_arry.ndim)
print(string_arry.shape) #Gives rows and columns
print(type(string_arry.shape))
print(string_arry.itemsize)
print(string_arry.nbytes) #itemsize * size => 28 * 8
print(string_arry[0, -2]) #Sunny
print(string_arry[:, -1]) # Lucky Josyula
print(type(string_arry[:, -1]))

print(np.identity(3))
string_arry.tolist()

