	
def merge_sort(array_1, array_2):
	array_final = list()

	length_of_array_1 = len(array_1)
	length_of_array_2 = len(array_2)
	
	i = j = 0

	while(i < length_of_array_1 and j < length_of_array_2):
		if array_1[i] < array_2[j]:
			array_final.append(array_1[i])
			i += 1
		
		else: 
			array_final.append(array_2[j])
			j += 1

	if j >= length_of_array_2:
		while (i < length_of_array_1):
			array_final.append(array_1[i])
			i += 1

	elif i >= length_of_array_1:
		while (j < length_of_array_2):
			array_final.append(array_2[j])
			j += 1

	return array_final 



print("here")

a_1 = [0,4,6,7,9]
a_2 = [3,6,8,9]
print(merge_sort(a_1, a_2))
				


