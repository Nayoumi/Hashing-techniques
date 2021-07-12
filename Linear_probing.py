#implementing linear probing using hashing
import numpy as np
def creatingHash(array,none): # creating hash function using linear probing
  for i in range(len(array)):
    keys = array[i] % 10 # calculating the hash function using mod function
    if none[keys] == None : #if the index is empty than number is inserted
      none[keys] = array[i] # the key value mapped to hash table and none is replaced with key value
    else:
      keys = (keys +1)%10 # if above condition is false linear hash function is implemented 
      #print(keys)
      while (none[keys]!= None): # while loop is iterated till the hash table consits of none
        keys =keys +1 # the key value is in cremented to compare with the next index is none or not
      if none[keys] == None: # if key is found empty the none is replaced withe the hashed key value
        none[keys] =array[i]
  searchHash(none) # calling the search function
  deleteHash(none) # calling the delete function
def searchHash(none):
  user_input = int(input("Enter the number to search : ")) # asking for the user input
  for i in range(len(none)):
    if (user_input == none[i]): # if user input is equal to the value in hash table than the value is printed
      print("The number is found : ",none[i])
      break
    elif (user_input != none[i]): # if above condition is failed the value is not printed
     print("The number is not found : ",none[i])
def deleteHash(none):
  user_input = int(input("Enter the number to delete : ")) # asking dor the user input
  for i in range(len(none)):
    if (user_input == none[i]):# if user input is equal to the value in hash table than the value is repaced with None without decresing the table size
      print("The number is found : ",none[i])
      none[i] = None
      #print(none)
      break
    else: # if above condition is failed the value is not replaced
     print("The number is not found : ",none[i])
array =[133,43,53,63,59,9,39,10,20]
none = [None]*10
creatingHash(array,none) # calling the hash function with two arguments passing
print (np.array(none)) #printing the hash table
