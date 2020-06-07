
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
  		address = self.__hash(key)
  		self.data[address] = value
  		return None

	def get(key):
  		address = self.__hash(key)
  		return self.data[address]




