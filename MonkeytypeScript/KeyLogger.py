import threading
import queue
from pynput import keyboard


q = queue.Queue()
a = []


def writer():
	while True:
		item = q.get()
		i = str(item)
		if len(i) == 3:
			a.append(i[1])

		if item == keyboard.Key.space:
			a.append(' ')
		if item == keyboard.Key.backspace:
			a.pop()
		if item == keyboard.Key.enter:
			a.append('\n')
		if item == keyboard.Key.end:
			break

	with open('output.txt', 'w', encoding='utf-8') as f:
		s = ''.join(a)
		f.write(s)



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
