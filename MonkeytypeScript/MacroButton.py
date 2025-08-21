import threading
import queue
from pynput import keyboard
import Macro

q = queue.Queue()

def writer():
	macro = Macro.TypeMacro()
	while True:
		key = q.get()
		if key == keyboard.Key.f12:
			# macro.type_test()
			macro.type_from_screen()
		if key == keyboard.Key.end:
			break




def reader():
	with keyboard.Listener(on_press=on_press, on_release=on_release) as l:
		l.join()


def on_press(key):
	try:
		q.put(key)
	except AttributeError:
		print(f'Special {key} is pressed')


def on_release(key):
	if key == keyboard.Key.end:
		return False
	return None


re = threading.Thread(target = reader)
wr = threading.Thread(target= writer)
re.start()
wr.start()
re.join()
wr.join()
