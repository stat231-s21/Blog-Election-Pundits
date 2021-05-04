import os

def substr_at(s, pattern, index):
    l = len(pattern)
    return s[index:index+l] == pattern

file_names = os.listdir()

speech_file_names = []
for file_name in file_names:
    if "-" in file_name:
        speech_file_names.append(file_name)

for file_name in speech_file_names:
    with open(file_name) as f:
        text = f.read()
    
    extracted = [] # a list of chars
    # iterate over the text and extract stuff
    for i in range(len(text)):
        if substr_at(text, "Biden: (", i):
            # extract the text
            while 
