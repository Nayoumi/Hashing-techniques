#Double hashing probing
import numpy as np
def doubleHash(double_array,double_none):
  prime = []
  k = 1
  for j in range(2,len(double_none)):
    if (j % 2 != 0 and j % 3 != 0 and j<len(double_none)):
      prime.append(j)
  max_prime = max(prime)
  for i in range(len(double_array)):
    keys = double_array[i] % 10
    if (double_none[keys] == None):
      double_none[keys] = double_array[i]
    else:
      keys =  k * (max_prime - (keys % max_prime))
      while (double_none[keys] != None):
        k = k + 1
        break
      if (double_none[keys] == None):
        double_none[keys] = double_array[i] 
  searchDouble(double_none)
  deleteDouble(double_none)
def searchDouble(double_none):
  user_input = int(input("Enter the number to search : ")) # asking for the user input
  for i in range(len(double_none)):
    if (user_input == double_none[i]): # if user input is equal to the value in hash table than the value is printed
      print("The number is found : ",double_none[i])
      break
    elif (user_input != double_none[i]): # if above condition is failed the value is not printed
     print("The number is not found : ",double_none[i])
def deleteDouble(none):
  user_input = int(input("Enter the number to delete : ")) # asking dor the user input
  for i in range(len(double_none)):
    if (user_input == double_none[i]):# if user input is equal to the value in hash table than the value is repaced with None without decresing the table size
      print("The number is found : ",double_none[i])
      double_none[i] = None
      #print(none)
      break
    else: # if above condition is failed the value is not replaced
     print("The number is not found : ",double_none[i])
double_array = [133,43,59,9,39,53,64]
double_none =[None]*10
doubleHash(double_array, double_none)
print(np.array(double_none))
