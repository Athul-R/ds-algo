"""

This file implements a function that would reverse a string. 


"""

def reverse_string(string: str):
	length = len(string)
	
	for i in range(length//2):
		temp = string[i]
		string[i] = string[length - 1 - i]
		string[length - 1 - i] = temp

	return string


if __name__ ==  "__main__":
 
 string = "my name is Khan"
 print(reverse_string(string))
