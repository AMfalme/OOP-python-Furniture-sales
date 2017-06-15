from abc import ABCMeta, abstractmethod



class Electronics(object):
	"""docstring for Electronics
	This is an abstract Base class for a vendor selling Electronics of various types.

	"""
	__metaclass__ = ABCMeta
	def __init__(self, make, year_of_manufacture, sale_date, purchase_price, selling_price, purchase_date):
		super(Electronics, self).__init__()
		self.make = make
		self.year_of_manufacture = year_of_manufacture
		self.sale_date = sale_date
		self.purchase_price = purchase_price
		self.selling_price
	def profit_after_sale(self):
		profit = self.selling_price - self.purchase_price
		return profit

	def make(self):
		return self.make

	@abstractmethod
	def type_of_electronic(self):
		return self.make


class computer(Electronics):
	"""docstring for computer"""
	def __init__(self, model):
		self.model = model
	def type_of_electronic(self):
		return "Computer"
	def insert_ram_capacity(self):
		ram_in_gb = raw_input("What is the ram of this computer")
		self.ram = ram_in_gb
		return self.ram

	def Insert_processor_capacity(self):
		processor = raw_input("kindly input the processor capacity on this computer")
laptop = computer("HP")

print(laptop.make)
		
		
		