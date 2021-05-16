# this program produces two csv outputs, one for Biden, and one for Trump.
# Each csv file contains the columns word1, word2, and weight, where weight is the number of times that word1 occurs within `dist` words of word2. Only the `num_words_considered` most common words are considered.

import os
import re
from collections import defaultdict

# put stopwords into a dictionary
with open('stopwords.txt') as f:
    stopwords = set(f.read().splitlines())

dist = 50

output_files = ["biden_speeches", "trump_speeches"]

for output_file in output_files:
    output = [] # each element is one line of the csv output
    output.append("word1,word2,weight")
    output_dictionary = defaultdict(lambda: 0) # maps frozenset (of two strings) to int
    os.chdir(output_file)
    input_files = os.listdir()

    topics_dict = dict()
    topics_dict['covid'] = 'Covid'
    topics_dict['virus'] = 'Covid'
    topics_dict['coronavirus'] = 'Covid'
    topics_dict['gun'] = 'Guns'
    topics_dict['guns'] = 'Guns'
    topics_dict['trade'] = 'Trade'
    topics_dict['college'] = 'Education'
    topics_dict['education'] = 'Education'
    topics_dict['student'] = 'Education'
    topics_dict['immigration'] = 'Immigration'
    topics_dict['health'] = 'Health Care'
    topics_dict['healthcare'] = 'Health Care'
    topics_dict['climate'] = 'Climate Change'
    topics_dict['environment'] = 'Climate Change'
    topics_dict['abortion'] = 'Abortion'
    topics_dict['economy'] = 'Economy'
    topics_dict['iran'] = 'Iran'

    frequencies = defaultdict(lambda: 0)

    for input_file in input_files:
        with open(input_file) as f:
            text = f.read()

        regex = re.compile('[^a-zA-Z\' ]')
        text = regex.sub('', text)

        words = re.split(' +|: |, |-|\. ', text)
        for i in range(len(words)):
            word = words[i].lower()
            if word not in topics_dict.keys():
                continue

            frequencies[topics_dict[word]] += 1
            
            # acquire nearby words
            nearby_words = []
            for j in range(i - dist, i + dist + 1): # check all j within `dist` of word
                if j >= 0 and j < len(words) and j != i: # if j is a valid index
                    if words[j] in topics_dict.keys() and topics_dict[words[j]] != topics_dict[word]:
                        nearby_words.append(words[j])

            # increase weights accordingly
            for nearby_word in nearby_words:
                # create hashable frozenset object
                to_hash = frozenset([topics_dict[word], topics_dict[nearby_word]])
                output_dictionary[to_hash] += 1

    for pair_set in output_dictionary.keys():
        pair_list = list(pair_set)
        weight = output_dictionary[pair_set]
        output.append(pair_list[0] + ',' + pair_list[1] + ',' + str(weight))

    output = '\n'.join(output)

    os.chdir("..")

    with open(output_file + "_network_data.csv", 'w') as f:
        f.write(output)
