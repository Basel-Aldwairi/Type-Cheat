from pynput import keyboard
import time
import random
time.sleep(2)

kb = keyboard.Controller()
s = 'Instead of wishing fervently, it would be faster to simply fix your eyes on your goal and get moving.'
a = s.split()
for c in a:
	kb.type(c)
	r = random.random()
	time.sleep(r+0.5)
	kb.tap(keyboard.Key.space)

# time.sleep(2)
kb.tap(keyboard.Key.enter)
