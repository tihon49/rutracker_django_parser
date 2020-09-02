import requests
from django.core.management import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        '''проверка прокси на валидность'''
        with open('proxy.txt') as file:
            proxy_base = ''.join(file.readlines()).strip().split('\n')

        good_list = []

        for proxy in proxy_base:
            proxies = {'http': f'http://{proxy}:8080',
                       'https': f'http://{proxy}:8080'}
            link = 'https://rutracker.org/'
            try:
                response = requests.get(link, proxies=proxies, timeout=3)
                if proxy not in good_list:
                    good_list.append(proxy)
                    print(f'GOOD: {proxy}')
            except:
                print('Прокси не валидный')

            with open('goods.txt', 'w') as file:
                for proxy in good_list:
                    file.write(f'{proxy}:8080' + '\n')
        print('Done')