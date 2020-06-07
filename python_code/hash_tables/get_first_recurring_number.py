from typing import List

def first_occurence_char(input_: List) -> Union[str, None]:
	
	hash_ = dict()
	for item in input_:
		if hash_.get(item, None):
			return item

		hash_[item] = 0

	return None


