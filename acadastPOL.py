import discord
from discord.ext import commands
import os
import urllib.request
import discord
from discord.ext import commands
import os
from discord.utils import get
import requests
import responses
import aiohttp
from aiohttp import request
import time
import asyncio
from mojang import MojangAPI
import json
import urllib, json
import maya
from datetime import date
from random import choice
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import re
import random
from random import choice
import fake_useragent

from discord.ext import commands
import pymongo
from pymongo import MongoClient
from datetime import datetime

from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import fake_useragent
from time import sleep
#########

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from random import randint
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import os


vk_session = vk_api.VkApi(token=os.environ['token'])
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)
msg = '521800800844'

print('bot start')
def send_some_msg(id, some_text):
    vk_session.method("messages.send", {"user_id":id, "message":some_text,"random_id":0})


def grass_block(region='52',district='18',zone='0080065',grass='13',blockX='56.265263472603515',blockY='43.996875286102295'):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    
    browser.get(f'https://egrpmap.ru/?cadNumber={region}%3A{district}%3A{zone}%3A{grass}&lat={blockX}&lng={blockY}&zoom=17')
    
    subtitle = browser.find_elements_by_class_name('cadr-map-info-b__subtitle')
    title = browser.find_elements_by_class_name('cadr-map-info-b__title')
    tabs = browser.find_elements_by_class_name('cadr-map-info-b__info-table')
    try:
        super_text = f'{title[0].text}\n{subtitle[0].text}\n'
        for table in tabs:
            super_text += table.text + '\n'
        super_text += f'https://egrpmap.ru/?cadNumber={region}%3A{district}%3A{zone}%3A{grass}&lat={blockX}&lng={blockY}&zoom=17'
    except IndexError:
        browser.quit()
        return 'index error'
    browser.quit()
    return super_text

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            send_some_msg(id,grass_block(region=msg[0:2],district=msg[2:4],zone=msg[4:-1],grass=msg[11:]))

