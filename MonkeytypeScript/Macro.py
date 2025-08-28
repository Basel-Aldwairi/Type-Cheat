import time

from pynput import keyboard
import ImageProcessing

class TypeMacro:
	def __init__(self):
		self.kb = keyboard.Controller()

	def type_test(self):
		s = 'This is a test'
		for c in s:
			self.kb.type(c)

	def type_from_screen(self,region):
		s = ImageProcessing.get_text(region)
		for c in s:
			# time.sleep(0.1)
			self.kb.press(c)
			# time.sleep(0.05)
			self.kb.release(c)

#
# macro = TypeMacro()
# macro.type_test()