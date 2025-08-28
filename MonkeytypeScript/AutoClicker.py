from pynput.mouse import Button, Controller
import time

class AutoClicker:

	def __init__(self):
		self.active = False
		self.time_between = 0.05
		self.controller = Controller()
		self.time_on = True

	def auto_click(self):
		# self.start_auto_clicker()
		while self.active:
			if self.time_on:
				time.sleep(self.time_between)
			# print('herer')
			self.controller.click(Button.left, 1)

	def set_auto_click_time(self,time_between_clicks):
			self.time_between = time_between_clicks

	def start_auto_clicker(self):
		self.active = True
		self.auto_click()

	def end_auto_clicker(self):
		self.active = False

	def is_active(self):
		return self.active

