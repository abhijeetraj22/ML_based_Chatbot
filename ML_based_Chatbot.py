import chatterbot

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from chatterbot import *
#from tkinter import *
#import pyttsx3 as pp
#import speech_recognition as s
#import os
#from nltk.corpus import wordnet
#import spacy

bot = ChatBot("My Bot")

convo = [
    'hello',
    'hi there !',
    'What is your name ?',
    'My name is Bot , i am created by Kanishka Gour',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in lucknow',
    'In which language you talk?',
    ' I mostly talk in english'
]

trainer = ListTrainer(bot)

trainer.train(convo)
answer = bot.get_response("What is your name")
print(answer)
print("Talk to bot")
while True:
    query = input()
    if query == 'exit':
        break
    answer = bot.get_response(query)
    print("bot : ", answer)
