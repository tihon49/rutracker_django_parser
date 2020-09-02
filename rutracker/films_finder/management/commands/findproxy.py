import requests
from bs4 import BeautifulSoup
from django.core.management import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        '''получение списка прокси с сайта'''
        url = 'https://hidemy.name/ru/proxy-list/?ports=8080&type=h#list'
        headers = {'accept': '*/*',
                   'user-agent': 'Mozilla/5.0(X11;Linux x86_64...)Geco/20100101 Firefox/60.0'}
        session = requests.session()
        response = session.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'lxml')
        main_div = soup.find('div', class_='table_block')

        proxy_list = []
        for line in main_div.find_all('tr'):
            proxy = line.find('td').text
            if proxy not in proxy_list:
                proxy_list.append(proxy)

        with open('proxy.txt', 'w') as out:
            for proxy in proxy_list:
                # print(proxy)
                out.write(proxy + '\n')
        print(f'Done. Total proxy count = {len(proxy_list)}')