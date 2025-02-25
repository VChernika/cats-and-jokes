from random import sample, randint, choice
from pprint import pprint
import requests
from time import sleep
from config import *
from settings import *



def send_media_group(chat_id, TOKEN, image_urls, joke):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMediaGroup'
    media = [{'type': 'photo', 'media': url} for url in image_urls]
    media[0]['caption'] = joke
    payload = {
        'chat_id': chat_id,
        'media': media
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()

def get_cat_image_urls(api_cats_token, a, b):
    
    cats_url = "https://api.thecatapi.com/v1/images/search"
    params_cats = {
        "limit": 10,
        "api_key": api_cats_token,
    }

    response_cats = requests.get(cats_url, params=params_cats)
    response_cats.raise_for_status()
    cats = sample(response_cats.json(), randint(a,b))

    cats_list = []
    for i in cats:
        cats_list.append(i['url'])
    return cats_list

def get_jokes_url():
    jokes_url = "http://shortiki.com/export/api.php"
    params_jokes = {
        "format" : "json",
        "type" : "top",
        "amount" : "100",
    }
    response_jokes = requests.get(jokes_url, params=params_jokes)
    response_jokes.raise_for_status()

    joke = sample(response_jokes.json(), 1)[0]["content"]
    return joke 


while True:
    cat_image_urls = get_cat_image_urls(api_cats_token, cats_count_from, cats_count_to)
    
    joke = get_jokes_url()


    send_media_group(tg_chat_id, tg_token, cat_image_urls, joke)
    sleep(delay)