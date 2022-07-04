#!/usr/bin/python3
class BaseGeometry:
	""" class that define the attribute of geometric  shape """
	def area(self):
		""" the method that define  the area of the geometric shape """
		raise Exception("area() is not implemented")
	def integer_validator(self, name, value):
		"""
		Method that recieves the vale property
		
		Args: 
			name: name of the object
			value: value of the property
		"""
		if type(value) is not int:
			raise TypeError("{} must be an integer".formst(name))
		if value<=0:
			raise ValueError("{} must be greater than 0".format(name))
