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
    
    extracted_text = []
    i = 0
    while i < len(text):
        if substr_at(text, ": (", i):
            # remove name of speaker back to previous period
            while len(extracted_text) != 0 and extracted_text[-1] != ".":
                extracted_text.pop()

            # increment i
            i += 3
            while text[i] != ")":
                i += 1
            i += 1

        else:
            extracted_text.append(text[i])
            i += 1

    extracted_text = ''.join(extracted_text)
    
    with open(file_name, 'w') as f:
        f.write(extracted_text)
