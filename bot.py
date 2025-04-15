import os
import tweepy
import requests
import random
Twitter auth

API_KEY = os.environ["TWITTER_API_KEY"] API_SECRET = os.environ["TWITTER_API_SECRET"] ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"] ACCESS_SECRET = os.environ["TWITTER_ACCESS_SECRET"]

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET) api = tweepy.API(auth)

def get_fact(): r = requests.get("https://uselessfacts.jsph.pl/random.json?language=en") return r.json()["text"]

def get_quote(): r = requests.get("https://api.quotable.io/random") data = r.json() return f'"{data["content"]}" — {data["author"]}'

def get_joke(): r = requests.get("https://official-joke-api.appspot.com/jokes/random") data = r.json() return f'{data["setup"]} {data["punchline"]}'

def get_advice(): r = requests.get("https://api.adviceslip.com/advice") return r.json()["slip"]["advice"]

def get_word(): r = requests.get("https://random-word-api.herokuapp.com/word?number=1") return f'Word of the day: {r.json()[0]}'

def get_meme(): r = requests.get("https://meme-api.com/gimme") data = r.json() return data["title"] + " " + data["url"]

options = [get_fact, get_quote, get_joke, get_advice, get_word, get_meme] selected = random.choice(options) tweet = selected()

Make sure tweet is within 280 characters

if len(tweet) > 280: tweet = tweet[:277] + "..."

api.update_status(tweet)

