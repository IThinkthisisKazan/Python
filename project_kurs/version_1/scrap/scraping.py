from bs4 import BeautifulSoup  # для парсинга старниц
import requests                # для запросов к сайту, получения содержимого веб-страницы
from requests import get
import urllib3
import certifi
import time
import os
import random


'''
def create_file():
    input_file = open('output.txt', encoding='utf-8')
    output_file = open('nameOfbody.txt', 'w', encoding="utf-8")
    for line in input_file:
        line = line.strip().split(', ')
        print(line)
        if line != ['']:
            right_answer = line[-3]
            output_file.write("%s\n" % right_answer)
    input_file.close()
    output_file.close()
'''





def main():
    url = 'https://www.avito.ru/yoshkar-ola/avtomobili?cd=1&radius=200&proprofile=1&p='
    auto = []
    body = []
    data = []
    image = []
    #http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    count = 2
    while count <= 5:
        url = 'https://www.avito.ru/yoshkar-ola/avtomobili?cd=1&radius=200&proprofile=1&p=' + str(count)
        print(url)
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        auto_data = html_soup.find_all('div', class_="item__line")
        # find image
        count = 0
        for image in html_soup.find_all('img', alt= True):
            # print image source
            try:
                name_auto = str(image['alt'])

                print(name_auto)
                subdir = name_auto.strip().split(', ')
                subdir = subdir[-4]
                '''
                for word in subdir.split(' '):
                    subdir = word
                    print(subdir)
                    '''
                if not os.path.exists('upload/' + subdir):
                    os.mkdir('upload/' + subdir)
                image_url = str(image['src'])
                print(image_url)
                if (image_url.endswith(".jpg") and image_url.startswith("https://")):
                    print(image_url)
                    image_url = requests.get(image_url).content

                with open('upload/' + subdir + '/' + name_auto, 'wb') as handler:
                    handler.write(image_url)
            except IndexError:
                continue

        if auto_data != []:
            auto.extend(auto_data)
            value = random.random()
            scaled_value = 1 + (value * (7 - 5))
            print(scaled_value)
            time.sleep(scaled_value)
        else:
            print('empty')
            break
        count += 1

    print()

    n = int(len(auto)) - 1
    count = 0
    while count <= 4:  # count <= n
        info = 	auto[int(count)]
        price = info.find('span', {"class":"snippet-price"}).text
        title = info.find('span', {"class":"snippet-link-name"}).text
        body = info.find('div', {"class":"specific-params specific-params_block"}).text
        data.append(body)
        with open('output.txt', 'w', encoding='utf-8') as filehadle:
            filehadle.writelines(links for links in data)
        print(price, title, body)
        count += 1



if __name__ == '__main__':
    main()
    #create_file()