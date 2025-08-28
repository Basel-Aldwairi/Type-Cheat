import threading
import queue
import sys
from pynput import keyboard
import Macro
import AutoClicker as AC
import MousePosition

printing_lock = threading.Lock()
ac = AC.AutoClicker()
# ac.time_on = False
# ac.time_between = 0.01
macro = Macro.TypeMacro()
kb_controller = keyboard.Controller()
stop_event = threading.Event()
region = ()

def run_in_thread(func):
	threading.Thread(target = func, daemon=True).start()

def auto_click():
	if not ac.is_active():
		ac.start_auto_clicker()
	else:
		ac.end_auto_clicker()


def print_from_screen():
	if printing_lock.acquire_lock(blocking=False):
		try:
			print('took lock')
			run_in_thread(print_in_thread)
		finally:
			pass
			# print('released lock')
			# printing_lock.release()

def print_in_thread():
	kb_controller.release(key=keyboard.Key.ctrl)
	kb_controller.release(key=keyboard.Key.alt)
	macro.type_from_screen(region)
	print('released lock')
	printing_lock.release()



def end_macros():
	stop_event.set()
	sys.exit(0)

def set_region():
	global region
	region = MousePosition.get_pos()
	print(region)



hotkeys = {
	'<ctrl>+<alt>+a' : lambda: run_in_thread(auto_click),
	'<ctrl>+<alt>+]' : lambda: print_from_screen(),
	'<ctrl>+<alt>+g' : lambda: run_in_thread(set_region),
	'<ctrl>+<alt>+<end>' : lambda: end_macros()
}

hotkey_objects = [
	keyboard.HotKey(keyboard.HotKey.parse(combo),action)
	for combo, action in hotkeys.items()
]

def for_canonical(f):
	return lambda k: f(listener.canonical(k))

with keyboard.Listener(
	# on_press=None,
	on_press=lambda k: [for_canonical(h.press)(k) for h in hotkey_objects],
	on_release= lambda  k: [for_canonical(h.release)(k) for h in hotkey_objects]
) as listener:
	print('listening')
	listener.join()

