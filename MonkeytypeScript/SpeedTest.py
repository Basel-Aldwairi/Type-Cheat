from colorama import Fore as Color
import os
import readchar
import time
from PossibleWords import filtered_words, filtered_words_len
import random as rn

MAX_WORDS = 20


# original_string = 'This is a test and a very long string lets see how itll work'
original_string_array = []

for _ in range(MAX_WORDS):
	random_index = int(rn.random() * filtered_words_len)
	chosen_word = (filtered_words[random_index])
	original_string_array.append(chosen_word)


original_string = ' '.join(original_string_array)
print(Color.LIGHTBLACK_EX + original_string)
# original_string_array = original_string.split()
original_string_word_count = len(original_string_array)
written_string = []
original_string_length = len(original_string)


writing = True
index = 0
word_index = 0
last_correct = 0
start_flag = True
start_time = 0
current_word = 0

while writing:
	char = readchar.readchar()
	os.system('cls')

	if start_flag:
		start_flag = False
		start_time = time.time()


	if char == '\x08':
		if written_string:
			written_string.pop()
			index -= 1


	elif char == ' ':
		# print('here')
		# print(written_string)
		# print(original_string_array[current_word])
		if ''.join(written_string) == original_string_array[current_word]:
			word_index = word_index + index + 1
			index = 0
			current_word += 1
			written_string = []

	else:
		written_string.append(char)
		index += 1


	if not written_string:
		index = 0
		last_correct = -1

	for i in range(index):
		# print(f'ws = {written_string[i]} os = {original_string[word_index + i]}')
		if written_string[i] == original_string[word_index + i]:
			last_correct = i
			if word_index + last_correct + 1 == original_string_length:
				writing = False
		else:
			break



	# print(f'in = {index} lc = {last_correct}')
	print(Color.GREEN + original_string[:word_index + last_correct + 1], end='')
	# print(color.RED + original_string[word_index + last_correct+1:word_index + index], end='')
	print(Color.RED + ''.join(written_string)[last_correct + 1:], end='')
	print(Color.LIGHTBLACK_EX + original_string[word_index + index:])
	# print(f'{''.join(written_string)}|')


end_time = time.time()
duration = end_time - start_time
words_per_minute = original_string_word_count/(duration/60)

print(f'Finished in {duration:.2f}s')
print(f'Words per Minute {words_per_minute:.2f}')