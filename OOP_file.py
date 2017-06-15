from abc import ABCMeta, abstractmethod



class Furniture(object):
	"""docstring for Furniture
	This is an abstract Base class for a vendor selling furniture of various types.

	"""
	def __init__(self, arg):
		super(Furniture, self).__init__()
		self.arg = arg
		