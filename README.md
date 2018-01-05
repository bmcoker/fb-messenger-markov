# Facebook Messenger Markov Chain Generator
Create Markov chains from Facebook messages and simulate conversations. This was thrown together for fun and not heavily-tested yet, but I haven't found a case where it doesn't work.

## Requirements
* Python 3.6 or greater
* BeautifulSoup

```
pip install BeautifulSoup
```

* Markovify

```
pip install Markovify
```

* A downloaded copy of your Facebook data, generated from [the link on the Settings page](https://www.facebook.com/settings)

## Usage
Go into the messages directory in your Facebook data and find the file containing the messages that you want.

```
python fb_parse.py 123.html
```

Once fb_parse finishes running, you should have a new folder that contains filenames that are the names of each person in the conversation. You can use some or all of those with markov_conversation.py to simulate a conversation.

```
python markov_conversation.py me.txt you.txt him.txt her.txt
```
