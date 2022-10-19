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

#### Decode

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
creates a link that needs to be clicked to retrieve the refresh token.

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
#### Decode

## Discord

### Authentication
For the Discord covert channels a discord_config.py file is needed that contains the following:

```python
token = "Example Token"
```

### Binary Covert Channel
#### Encode
This script collects the most recent 500 messages in the general channel, prompts for a message input, and converts that
message into binary. The script then adds a thumbs down reaction to signify a 0 and adds a thumbs up emoji to signify a 
1 to send the message. 
#### Decode
This script collects the most recent 500 messages in the general channel then checks each message for if a certain user 
added a thumbs up or thumbs down reaction. If the user added a thumbs up reaction the script adds a 1 to the binary 
string and if the user added a thumbs down reaction the script adds a 0. It then converts the binary string to ASCII and
returns the hidden message.
### Plaintext Covert Channel
#### Encode
#### Decode
