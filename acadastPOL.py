from random import randint
from selenium import webdriver  
from selenium.webdriver.firefox.options import Options
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import os


vk_session = vk_api.VkApi(token=os.environ['token'])
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)
msg = '521800800844'


def send_some_msg(id, some_text):
    vk_session.method("messages.send", {"user_id":id, "message":some_text,"random_id":0})


def grass_block(region='52',district='18',zone='0080065',grass='13',blockX='56.265263472603515',blockY='43.996875286102295'):
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get(f'https://egrpmap.ru/?cadNumber={region}%3A{district}%3A{zone}%3A{grass}&lat={blockX}&lng={blockY}&zoom=17')
    
    subtitle = browser.find_elements_by_class_name('cadr-map-info-b__subtitle')
    title = browser.find_elements_by_class_name('cadr-map-info-b__title')
    tabs = browser.find_elements_by_class_name('cadr-map-info-b__info-table')
    super_text = f'{title[0].text}\n{subtitle[0].text}\n'
    for table in tabs:
        super_text += table.text + '\n'
    super_text += f'https://egrpmap.ru/?cadNumber={region}%3A{district}%3A{zone}%3A{grass}&lat={blockX}&lng={blockY}&zoom=17'
    browser.quit()
    return super_text

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            grass_block(region=msg[0:2],district=msg[2:4],zone=msg[4:-1],grass=msg[11:12])

