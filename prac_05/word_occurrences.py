text = input("Text: ")
text_list = text.split(" ")
words_to_counts = {}
for words in text_list:
    if words not in words_to_counts:
        words_to_counts[words] = 1
    else:
        words_to_counts[words] += 1
for key,value in sorted(words_to_counts.items()):
    print("{:{}} : {}".format(key, 10, value))







