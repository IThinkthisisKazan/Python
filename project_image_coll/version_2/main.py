import urllib

from PIL.Image import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from bs4 import BeautifulSoup  # для парсинга старниц
import requests                # для запросов к сайту, получения содержимого веб-страницы
import os


def rnd_time_wait():
    value = random.random()
    scaled_value = 1 + (value * (7 - 5))
    return scaled_value


def img_save(sub, theme):
    try:
        os.mkdir("downloads" + '/' + theme  )
    except FileExistsError:
        pass

    count = 0
    for i in sub:
        src = i.get_attribute('src')
        try:
            if src != None:
                src = str(src)
                print(src)
                count += 1
                urllib.request.urlretrieve(src, os.path.join('downloads' + '/' + theme, 'image' + str(count) + '.jpg'))
            else:
                raise TypeError
        except TypeError:
            print('fail')


def dogs():
    theme = "Собаки"
    path = r"N:\STUDY_2\Python\project_kurs\version_2\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    driver.get('https://google.com')
    search_box_dogs = driver.find_element_by_css_selector('input.gLFyf') # нашли поисковую строку
    search_box_dogs.send_keys('Собаки') # вводим поисковый запрос
    search_box_dogs.send_keys(Keys.ENTER)
    driver.find_element_by_partial_link_text('Картинки').click()

    # код предназначен для прокрутки страницы вниз для загрузки всех изображений
    value = 0
    for i in range(20):
        driver.execute_script("scrollBy(" + str(value) +", +1000); ")
        value += 1000
        time.sleep(3)

    elem1 = driver.find_element_by_id('islmp') # Получить элемент по идентификатору со значением islmp.
    sub = elem1.find_elements_by_tag_name("img")

    img_save(sub, theme)

def cats():
    theme = "Кошки"
    path = r"N:\STUDY_2\Python\project_kurs\version_2\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    driver.get('https://google.com')
    search_box_dogs = driver.find_element_by_css_selector('input.gLFyf')  # нашли поисковую строку
    search_box_dogs.send_keys('Кошки')  # вводим поисковый запрос
    search_box_dogs.send_keys(Keys.ENTER)
    driver.find_element_by_partial_link_text('Картинки').click()

    # код предназначен для прокрутки страницы вниз для загрузки всех изображений
    value = 0
    for i in range(20):
        driver.execute_script("scrollBy(" + str(value) + ", +1000); ")
        value += 1000
        time.sleep(3)

    elem1 = driver.find_element_by_id('islmp')  # Получить элемент по идентификатору со значением islmp.
    sub = elem1.find_elements_by_tag_name("img")

    img_save(sub, theme)


def main():
    dogs()
    time.sleep(5)
    cats()


if __name__ == '__main__':
    main()
