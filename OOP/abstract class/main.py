# membuat class abstract
# abc = abstract base class
from abc import ABC, abstractmethod

class Button(ABC): # inherit dari abc.ABC

	@abstractmethod
	def click(self):
		pass

class PushButton(Button):
	def click(self):
		print("push button click")

class RadioButton(Button):
	def click(self):
		print("radio button click")

tombol2 = PushButton()
tombol1 = RadioButton()
tombol2.click()
tombol1.click()
