# CSEC 791 MS Project - Grace Lombardi

This project is my Computing Security Master Degree Project at Rochester Institute of Technology. The paper that corresponds with this code can 
be found here: <Insert Link Here>

## Twitter

### Authentication
For the Twitter covert channels a twitter_config.py file is needed that contains the following:

```python
api_key = "Example API Key"
api_secret = "Example API Secret"
access_token = "Example Access Token"
access_secret = "Example Access Secret"
bearer_token = "Example Bearer Token"
client_id = "Example Client Id"
client_secret = "Example Client Secret"
```

### Binary Covert Channel
#### Encode
This script collects all the tweets of a given user, prompts for a message input, and converts that message into binary. 
The script then unlikes a tweet to signify a 0 and likes a tweet to signify a 1 to send the message. 
#### Decode
This script collects all the tweets of a given user then checks each tweet for if a certain user liked it. If the user 
liked it the script adds a 1 to the binary string and if the user has not liked it the script adds a 0. It then converts
the binary string to ASCII and returns the hidden message.
### Plaintext Covert Channel
#### Encode
This script first authenticates with Twitter and prompts for a message input. It then clears all the users bookmarks 
before encoding the message. Then the script loops through the message and searches recent tweets to find a tweet that 
starts with the military alphabet equivalent of that letter in the message. Once found the tweet is bookmarked and then 
the script moves onto the next letter in the message until it finishes them all.
#### Decode
This script first authenticates with Twitter and retrieves all bookmarks. Each bookmark is then looped through to add 
the first word of the tweet to a list. Those words are then converted to letters by using the military alphabet. These 
letters are then joined and reversed to reveal the hidden message.
## Facebook

### Authentication
For the Facebook covert channels a facebook_config.py file is needed that contains the following:

```python
```

### Binary Covert Channel
#### Encode
#### Decode
### Plaintext Covert Channel
#### Encode
#### Decode

## Reddit

### Authentication
For the Reddit covert channels a reddit_config.py file is needed that contains the following:

```python
client_id = "Example Client ID"
client_secret = "Example Client Secret"
user_agent = "script by /lombardig"
redirect_uri = "http://localhost:8080"
refresh_token = "Example Refresh Token"
```

#### Refresh Token
Run this script to create a refresh token. This script prompts the user for a client id and the client secret. It then 
creates a link that needs to be clicked to retrieve the refresh token. This script was written by Jean-Christophe 
Chouinard and was found here: https://www.jcchouinard.com/get-reddit-api-credentials-with-praw/

### Binary Covert Channel
#### Encode
This script prompts for a specific post id, prompts for a message input, and converts that message into binary. 
The script then comments "I disagree!" to signify a 0, "I agree!" to signify a 1, and "Boom!" to signify the end of a 
message.
#### Decode
This script collects all the comments on a specific post then checks each comment for its value. If the comment is "I 
disagree!" the script will add a 0 to the binary string, if it is "I agree!" the script will add a 1 to the binary 
string, and if it is "Boom!" the script will add a 9 to the binary string to signify the end of the message.
The script then converts the binary string to ASCII and returns the hidden message.

### Plaintext Covert Channel
#### Encode
This script first prompts for a message input and then authenticates with Reddit. Then the script loops through the 
message and adds a comment to a specified post with the military alphabet equivalent of that letter until it reaches the 
end of the message.
#### Decode
This script first authenticates with Reddit then retrieves all comments on a specific post. It then takes the first word
of the comment and uses the military alphabet to convert it to a letter. The letters are then all joined to reveal the 
hidden message.

## Discord

### Authentication
For the Discord covert channels a discord_config.py file is needed that contains the following:

```python
token = "Example Token"
```

### Binary Covert Channel
#### Encode
This script collects the most recent 500 messages in the general channel, waits for the word "message", prompts for a 
message input, and converts that message into binary. The script then adds a thumbs down reaction to signify a 0 and 
adds a thumbs up emoji to signify a 1 to send the message. 
#### Decode
This script waits for the word "history", collects the most recent 500 messages in the general channel, and checks each 
message for if a certain user added a thumbs up or thumbs down reaction. If the user added a thumbs up reaction the 
script adds a 1 to the binary string and if the user added a thumbs down reaction the script adds a 0. It then converts 
the binary string to ASCII and returns the hidden message.

### Plaintext Covert Channel
#### Encode
This script first prompts for a message input then takes each letter in that message and converts it to their military 
alphabet equivalent. The script then waits for the word "message" to be posted in the channel and sends the military 
alphabet words to the channel. It then sends "Boom!" to mark the end of the message.
#### Decode
This script waits for the word "history", collects the most recent 500 messages in the general channel, and then adds 
each message to a word list until the word "Boom!" is reached. It then converts the military alphabet words into their 
letter equivalent. Those letters are then joined and reversed to reveal the hidden message.

