from wordfreq import top_n_list

common_words = top_n_list('en',5000)
filtered_words = [w for w in common_words if len(w) in (3,4,5,6)]
filtered_words_len = len(filtered_words)

# print(filtered_words[:20])