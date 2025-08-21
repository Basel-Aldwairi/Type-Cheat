from pynput import keyboard
import ImageProcessing

class TypeMacro:
	def __init__(self):
		self.kb = keyboard.Controller()

	def type_test(self):
		s = 'This is a test'
		for c in s:
			self.kb.type(c)

	def type_from_screen(self):
		s = ImageProcessing.get_text()
		for c in s:
			self.kb.type(c)

#
# macro = TypeMacro()
# macro.type_test()