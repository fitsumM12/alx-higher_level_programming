#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
	"""Class that defines a rectangle from BaseGeometery class"""
	def __init__(self, width, height):
		"""Initialize instance"""
		self.integer_validator("width", width)
		self.integer_validator("height", height)
		self.__width = width
		self.__height = height
