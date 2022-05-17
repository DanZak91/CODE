from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

print(response.text)























# #Мы применили срез, чтобы получить последний элемент списка, в котором хранился весь список значений пагинации.
# from bs4 import BeautifulSoup
# import requests
#
# url = 'http://parsinger.ru/html/index1_page_3.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# shema = 'http://parsinger.ru/html/'

# pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]
#
# print(pagen)









# #извлекаем ссылки для страниц (пагинация)
# from bs4 import BeautifulSoup
# import requests
#
# url = 'http://parsinger.ru/html/index1_page_3.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
# # Обратите внимание на то как мы получаем значение атрибута href='', подобным образом мы можем извлекать ссылку из тегов <a>, такой подход  применим и к тегу <img>, мы сможем извлечь src='',
# # напомню что в src='' тега img хранится ссылка на изображения. Картинки мы будем парсить в следующих уроках.
# print(pagen)





# #https://stepik.org/lesson/700231/step/6?unit=700173
# from bs4 import BeautifulSoup
# import requests
#
# url = 'http://parsinger.ru/html/index1_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# price = sum([int(i.text.replace(' руб', '')) for i in soup.find_all('p', class_='price')])
# # или price = sum([int(x.text.split(' ')[0]) for x in soup.find_all('p', class_="price")])
# # или prices = [int(re.findall('\d+', p.text)[0]) for p in soup.find_all('p', class_='price')]
# print(price)




# # Поиск по атрибутам
# from bs4 import BeautifulSoup
# import requests
#
# url = 'http://parsinger.ru/html/headphones/5/5_32.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# div = soup.find('span', {'name': 'count'}).text
# print(div)









# # Поиск по id
# from bs4 import BeautifulSoup
# import requests
#
# url = 'http://parsinger.ru/html/headphones/5/5_32.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# div = soup.find('p', id='p_header').text
# print(div)



# #Поиск по class
# from bs4 import BeautifulSoup
# import requests
# url = 'http://parsinger.ru/html/headphones/5/5_32.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# div = soup.find('p', class_='article').text
# print(div)








# from bs4 import BeautifulSoup
# import requests, lxml
#
# #скачали с сайта zip.архив, сохранили в проект
# with open('html.zip', 'wb') as file_zip:
#     zip_file = file_zip.write(requests.get(url='http://parsinger.ru/downloads/cooking_soup/index.zip').content)
#
# with open('index.html', 'r', encoding='utf-8') as file:
#     soup = BeautifulSoup(file, 'lxml')
#     div = soup.find('div', 'item').find_all('li')
#     for i in div:
#         print(i.text)   # div = [x.text for x in soup.find('div', 'item').find_all('li')]







# import requests
#
# for i in range(1, 161):
#     response = requests.get(url=f'http://parsinger.ru/img_download/img/ready/{i}.png')
#     with open(f'imag{i}.png', 'wb+') as file:
#         file.write(response.content)




# import requests
# for i in range(1, 501):
#     url = f'http://parsinger.ru/task/1/{i}.html'
#     response = requests.get(url)
#     print(f"СЕКРЕТНЫЙ КОД --> {url}" if response.status_code == 200 else 'ОТВАЛ')




#
# import requests
# url = "http://parsinger.ru/video_downloads/videoplayback.mp4"
# response = requests.get(url=url, stream=True)
# with open('file.mp4', 'wb') as video:
#     for piece in response.iter_content(chunk_size=100000):
#         video.write(piece)
# #


# import requests
# from random import choice
# from fake_useragent import UserAgent
#
# url = 'http://httpbin.org/user-agent'
#
# for x in range(10):
#     ua = UserAgent()
#     fake_ua = {'user-agent': ua.random}
#     response = requests.get(url=url, headers=fake_ua)
#     print(response.text)


# import requests
# from random import choice
#
# url = 'http://httpbin.org/user-agent'
#
# while line := open('user_agent.txt').read().split('\n'):
#     user_agent = {'user-agent': choice(line)}
#     response = requests.get(url=url, headers=user_agent)
#     print(response.text)
