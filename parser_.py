from bs4 import BeautifulSoup
import requests

def get_html(base):
    html = requests.get(base).content
    return html

def main(html):
    soup = BeautifulSoup(html, 'lxml')
    article = soup.find_all('article', class_= 'post_preview')
    title_information = {}
    tegs_list = []
    index = 0
    
    for item in article:
        title_urls = item.find('a', class_ = 'post__title_link')
        time = item.find('span', class_ = 'post__time')
        title_tegs = item.find_all('a', class_= 'hub-link')

        index += 1

        title_information[index] = {
            'url' : title_urls.get('href'),
            'text' : title_urls.getText(),
            'time' : time.getText(),
            'tegs' : tegs_list
        }
        
        for teg in title_tegs:
            tegs_list.append(teg.getText())
        tegs_list = []

    return title_information