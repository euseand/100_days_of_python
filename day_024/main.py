LETTER_SAMPLE_PATH = './Input/Letters/starting_letter.txt'
NAMES_LIST_PATH = './Input/Names/invited_names.txt'
OUTPUT_DIR_PATH = './Output/ReadyToSend'
PLACEHOLDER = '[name]'

with open(LETTER_SAMPLE_PATH, 'r') as infile:
    letter_sample = infile.read()

with open(NAMES_LIST_PATH, 'r') as infile:
    names = [name.strip() for name in infile.readlines()]
    for name in names:
        with open(f'{OUTPUT_DIR_PATH}/{name}.txt', 'w') as outfile:
            outfile.write(letter_sample.replace(PLACEHOLDER, name))
