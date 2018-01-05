'''
    Filename: fb_parse.py
    Author: Brett Coker
    Python Version: 3.6.4

    Given a Facebook Messenger file from a Facebook data export (named #.html),
    parses the file and outputs a .txt file for each member of the chat. The
    exported files will be named after the person whose messages they contain.
'''
import sys
import os
from bs4 import BeautifulSoup


def get_senders(soup):
    """Parses the user names from the Soup object."""
    raw_senders = soup.find_all('span', 'user')
    return [sender.text for sender in raw_senders]


def get_messages(soup):
    """Parses the messages from the Soup object."""
    raw_messages = soup.find_all('p')

    # There are two <p> tags for every message, so just get rid of the
    # odd-numbered ones
    raw_messages = raw_messages[1::2]

    return [message.text for message in raw_messages]


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} messages.html')
        sys.exit()

    filename = sys.argv[1]
    with open(filename, 'rb') as message_file:
        print('Loading the file...')
        soup = BeautifulSoup(message_file, 'html.parser')

    print('Parsing messages...')
    senders = get_senders(soup)
    messages = get_messages(soup)

    # This shouldn't happen, but if the lengths are different, this can't work
    if len(senders) != len(messages):
        print('Something went wrong :(')
        sys.exit()

    print('Putting it all together...')
    associations = {}
    for i in range(0, len(senders) - 1):
        # Make a key for a new user
        if senders[i] not in associations:
            associations[senders[i]] = []

        message = messages[i]
        associations[senders[i]].append(message)

    folder = f'{filename} data'
    os.mkdir(folder)

    for sender in associations:
        data_file = f'{folder}/{sender}.txt'

        with open(data_file, 'w') as outfile:
            for message in associations[sender]:
                try:
                    outfile.write(f'{message}\n')
                except UnicodeEncodeError:
                    encoded = message.encode('utf8')
                    outfile.write(f'{encoded}\n')

        print(f'Wrote {data_file}')

if __name__ == '__main__':
    main()
