# this program produces two csv outputs, one for Biden, and one for Trump.
# Each csv file contains the columns word1, word2, and weight, where weight is the number of times that word1 occurs within `dist` words of word2. Only the `num_words_considered` most common words are considered.

import os
import re
from collections import defaultdict

# put stopwords into a dictionary
with open('stopwords.txt') as f:
    stopwords = set(f.read().splitlines())

dist = 10
num_words_considered = 40

output_files = ["biden_speeches", "trump_speeches"]

for output_file in output_files:
    output = [] # each element is one line of the csv output
    output.append("word1,word2,weight")
    output_dictionary = defaultdict(lambda: 0) # maps frozenset (of two strings) to int
    os.chdir(output_file)
    input_files = os.listdir()

    #first, compile a set of the words to consider
    word_frequencies = defaultdict(lambda: 0)
    for input_file in input_files:
        with open(input_file) as f:
            text = f.read()
            
        regex = re.compile('[^a-zA-Z\' ]')
        text = regex.sub('', text)

        words = text.split(" ")
        for word in words:
            word = word.lower()
            if word not in stopwords and word != '':
                word_frequencies[word] += 1

    frequencies = [(num, word) for word, num in word_frequencies.items()]
    frequencies.sort()
    frequencies.reverse()
    
    top_words = set([word for num, word in frequencies[:num_words_considered]])

    for input_file in input_files:
        with open(input_file) as f:
            text = f.read()

        regex = re.compile('[^a-zA-Z\' ]')
        text = regex.sub('', text)

        words = text.split(" ")
        for i in range(len(words)):
            word = words[i].lower()
            if word not in top_words:
                continue
            
            # acquire nearby words
            nearby_words = []
            for j in range(i - dist, i + dist + 1): # check all j within `dist` of word
                if j >= 0 and j < len(words) and j != i: # if j is a valid index
                    if words[j] in top_words and words[j] != word:
                        nearby_words.append(words[j])

            # increase weights accordingly
            for nearby_word in nearby_words:
                # create hashable frozenset object
                to_hash = frozenset([word, nearby_word])
                output_dictionary[to_hash] += 1

    for pair_set in output_dictionary.keys():
        pair_list = list(pair_set)
        weight = output_dictionary[pair_set]
        output.append(pair_list[0] + ',' + pair_list[1] + ',' + str(weight))

    output = '\n'.join(output)

    os.chdir("..")

    with open(output_file + "_network_data_no_topics.csv", 'w') as f:
        f.write(output)
