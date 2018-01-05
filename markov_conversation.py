'''
    Filename: markov_conversation.py
    Author: Brett Coker
    Python Version: 3.6.4

    Given .txt files (minimum 2) as arguments, creates Markov models and
    simulates a conversation between them.

    The intent is for this to be used with the .txt files generated from
    fb_parse, where each message will be on a new line of the .txt files, and
    the filenames (without the extension) will be used as the names of each
    "person."
'''
import sys
import os
from random import randrange
from time import sleep
import ntpath
import markovify


def make_model(filename):
    """Creates a Markov model from a given file."""
    # Strip folders from name and get rid of .txt extension
    strip_path = ntpath.basename(filename)
    name = strip_path[:-4]

    with open(filename) as message_file:
        messages = message_file.read()

    model = markovify.NewlineText(messages)

    return {'name': name, 'model': model}


def main():
    if len(sys.argv) < 3:
        print(f'Usage: python {sys.argv[0]} person1.txt person2.txt ...')
        sys.exit()

    filenames = []
    for i in range(1, len(sys.argv)):
        filenames.append(sys.argv[i])

    print('Generating models...')

    models = []
    for filename in filenames:
        model = make_model(filename)
        models.append(model)

    os.system('cls' if os.name == 'nt' else 'clear')
    print('Starting message simulation. Ctrl+C to exit\n')

    while True:
        try:
            i = randrange(len(models))
            name = models[i]['name']
            sentence = models[i]['model'].make_sentence(tries=100)
            print(f'{name}: {sentence}')
            sleep(randrange(5, 15))
        except KeyboardInterrupt:
            sys.exit()


if __name__ == '__main__':
    main()
