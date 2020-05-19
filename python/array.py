"""

This file has the array implemention using Python Class. 

"""

class ArrayWithDict(object):
	"""
	This is the array implementation with data as the Dict Object

	"""
	def __init__(self, arg):
		self.data = {}
		self.length = 0

	def get(self, index):
		return self.data.get(index)

	def push(self, item):
		self.data[self.length] = item
		self.length += 1
		return self.length

	def pop(self):
		last_item = self.data[self.length-1]
		del self.data[self.length-1]
		self.length -= 1
		return last_item

	def delete(self, index):
		item = self.data[index]
		self.shift_items(index)
		return item

	def shift_items(self, index):
		for i in range(index, self.length):
			self.data[i] = self.data[i+1]

		del self.data[self.length-1]
		self.length -= 1

class ArrayWithList(object):
	"""
	This is the array implementation with data as the Dict Object

	"""
	def __init__(self, arg):
		self.data = list()
		self.length = 0

	def get(self, index):
		return self.data[index]

	def push(self, item):
		self.data[self.length] = item
		self.length += 1
		return self.length

	def pop(self):
		last_item = self.data[self.length-1]
		del self.data[self.length-1]
		self.length -= 1
		return last_item

	def delete(self, index):
		item = self.data[index]
		self.shift_items(index)
		return item

	def shift_items(self, index):
		for i in range(index, self.length):
			self.data[i] = self.data[i+1]
			
		del self.data[self.length-1]
		self.length -= 1





