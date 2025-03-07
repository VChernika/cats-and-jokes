# Cats and jokes

This is a telegram bot that automatically sends a random number of images with a random joke. And it does it all the time with a preset delay.
## How to install

Download and unzip the code. Python must already be installed. Then use pip to install the dependencies.

```
pip install -r requirements.txt
```

## How to launch

Create a file "config.py" and fill it out.
```
api_cats_token = " "
tg_token = " "
```

Write the api token to the "api_cats_token" variable 'https://thecatapi.com'. And in the "tg_token" variable, write the token from the telegram bot.

To run the program, you need to write in the terminal
```
python main.py
```

## How to set up the programm

All settings are in the file "settings.py ".

```
DELAY = 20
CATS_COUNT_FROM = 2
CATS_COUNT_TO = 5
TG_CHAT_ID = '@super_funny_cats'
```

- DELAY: Each time after the specified number of seconds, messages will be sent to telegram.
- CATS_COUNT_FROM: The minimum number of images per post.
- CATS_COUNT_TO: The maximum number of images per post. (Do not specify more than 10 images.)
- TG_CHAT_ID: ID of the Telegram channel. (Dot must be as an administrator in channel.)