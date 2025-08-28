# import pyautogui
from pynput import mouse
import time

def get_pos():
	button_state = {
		mouse.Button.left : False,
		mouse.Button.right : False,
		mouse.Button.middle : False
	}

	running = True
	start_index = True
	region = []


	def on_click(x,y,button,pressed):
		nonlocal start_index
		nonlocal region
		button_state[button] = pressed
		if button == mouse.Button.left:
			if start_index:
				region = [x,y]
			else:
				x_offset = abs(x - region[0])
				y_offset = abs(y - region[1])
				region[0] = min(x,region[0])
				region[1] = min(y,region[1])

				region.append(x_offset)
				region.append(y_offset)
				# print(region)
			start_index = not start_index



	listener =  mouse.Listener(on_click=on_click)
	listener.start()
	#
	region_tuple = 0
	while running:
		if len(region) == 4:
			if region[2] != 0 and region[3] != 0:
				running = False
				region_tuple = tuple(region)
		# print(button_state)
		pass
	# print(region_tuple)
	return region_tuple
# return region_tuple
# 	print(region)


