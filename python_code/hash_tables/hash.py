
class Hash(object):
	"""Hash tables using Class"""
	
	def __init__(self, size):
		self.data = list()
		self.size = size

	def __hash(key):
		hash = 0;
	    for i in range(len(key))
	        hash = (hash + ord(key[i]) * i) % self.size
	    
	    return hash;
  

  	def set(key, value):
  		hash_value = self.__hash(key)
  		self.data[hash_value] = value
  		return None

	def get(key):
  		hash_value = self.__hash(key)
  		return self.data[hash_value]




