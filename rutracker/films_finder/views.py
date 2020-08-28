import json
import os

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from rest_framework.response import Response
from rest_framework.views import APIView

from films_finder.models import Film
from films_finder.serializers import FilmSerializer
from rutracker.settings import BASE_DIR



def check_proxy():
    '''проверка прокси на валидность'''
    with open('proxy.txt') as file:
        proxy_base = ''.join(file.readlines()).strip().split('\n')
    for proxy in proxy_base:
        proxies = {'http': f'http://{proxy}:8080',
                   'https': f'http://{proxy}:8080'}
        link = 'https://rutracker.org/'
        try:
            response = requests.get(link, proxies=proxies, timeout=3)
            print(f'GOOD: {proxy}')
            with open('goods.txt', 'a') as f:
                f.write(f'{proxy}:8080' + '\n')
        except:
            print('Прокси не валидный')


def get_proxy():
    '''получение списка прокси с сайта'''
    url = 'https://hidemy.name/ru/proxy-list/?ports=8080&type=h#list'
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0(X11;Linux x86_64...)Geco/20100101 Firefox/60.0'}
    session = requests.session()
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    main_div = soup.find('div', class_='table_block')
    for proxy in main_div.find_all('tr'):
        p = proxy.find('td').text
        with open('proxy.txt', 'a') as out:
            out.write(p + '\n')


URL = 'https://rutracker.org/forum/viewforum.php?f=1950'


class FilmView(APIView):
    '''API вьюшка со всеми фильмами'''
    def get(self, request):
        queryset = Film.objects.all()
        serializer = FilmSerializer(queryset, many=True)

        with open(os.path.join(BASE_DIR, 'dump_data.json'), 'w', encoding='utf-8') as file:
            json.dump(serializer.data, file, indent=4, ensure_ascii=False)

        return Response(serializer.data)


def check_if_exist(name):
    '''функция проверки наличия фильма в бд'''
    # TODO: пока не работает
    if Film.objects.get(name=name):
        return True
    else:
        return False


def clear_description(description):
    '''функция получения описания фильма. встречается в фунции current_film_info()'''
    all_lines = [line for line in description.split('\n')]
    for index, line in enumerate(all_lines):
        if 'О фильме:' in line:
            descr = all_lines[index + 1]
            return descr
        elif 'Описание:' in line:
            descr = line.split('Описание:')[1]
            if len(descr) <= 1:
                descr = all_lines[index + 1]
            return descr
    return description


def get_soup(link):
    '''функция получения базовой информации со страницы'''
    #TODO:подключить сюда выбор прокси из goods.txt
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0(X11;Linux x86_64...)Geco/20100101 Firefox/60.0'}
    session = requests.session()

    proxies = {'http': 'http://177.36.128.162:8080',
               'https': 'http://177.36.128.162:8080'}
    response = session.get(link, headers=headers, proxies=proxies)
    soup = BeautifulSoup(response.content, 'lxml')
    return soup


def get_films_links(url) -> list:
    '''функция получения всех ссылок на фильмы с главной страницы'''
    films_links_list = []
    count = 0
    for page_num in range(1):
        soup = get_soup(url + f'&start={count}')
        count += 50
        main_div = soup.find('div', id='body_container')
        table = main_div.find('table', class_='vf-table vf-tor forumline forum')

        # tr всех филмов со страницы -> list
        main_tr = table.find_all('tr', class_='hl-tr')[1:]
        for item in main_tr:
            if item.find('div', class_='torTopic').find('a', class_='torTopic'):
                href = 'https://rutracker.org/forum/' + str(item.find('div', class_='torTopic').find('a', class_='torTopic').get('href'))
                print(href)
                films_links_list.append(href)
            else:
                print(f'Что-то не так с:\n{item}')
    return films_links_list


def current_film_info(films_links_list):
    '''функция получения информации конкретного фильма
       и создания объекта "фильм" в базе данных'''
    for link in films_links_list:
        try:
            soup = get_soup(link)
            main_div = soup.find('div', id='main_content_wrap')
            main_span = main_div.find('span', class_='post-font-serif1').text

            # на сайте имеется как минимум три вида страниц описания фильма
            # поэтому проверяем каждый из возможных вариантов
            if len(main_span.split('\n')) < 5:
                main_span = main_div.find('span', class_='post-font-serif2').text
                if len(main_span.split('\n')) < 5:
                   main_span = main_div.find('div', class_='post_body').text

            film_name = soup.find('h1', class_='maintitle').text.split('/')[0]
            image = main_div.find('var', class_='postImg postImgAligned img-right').get('title')
            description = clear_description(main_span)
            print('\n')

            # создадим модель фильма
            Film.objects.create(name=film_name, description=description,
                                url=link, image=image)
            print(f'Добавлен фильм: {Film.objects.get(name=film_name)}')
        except:
            pass
            # TODO: обработать ошибку 'NoneType' object has no attribute 'text'
            # print('\n' + '#' * 20)
            # print(f'{link} - {e}')
            # print('#' * 20 + '\n')


def get_new_films():
    '''функция наполненя БД фильмами'''
    # заново наполняем БД фильмами
    try:
        films_links_list = get_films_links(URL)
        current_film_info(films_links_list)
    except:
        pass


def reset_bd_view(request):
    '''вьюшка для обновления фильмов в БД'''
    # удаляем все фильмы из БД
    Film.objects.all().delete()
    # get_proxy()
    # check_proxy()
    get_new_films()
    return redirect('index_view')


def index_view(request):
    '''отображение всех фильмов из БД'''
    films = Film.objects.all()

    paginator = Paginator(films, 12)
    current_page = int(request.GET.get('page', 1))
    page_object = paginator.get_page(current_page)
    pages_count = paginator.num_pages
    prev_page, next_page = None, None

    if page_object.has_next():
        next_page = f'?page={page_object.next_page_number()}'
    if page_object.has_previous():
        prev_page = f'?page={page_object.previous_page_number()}'

    context = {'films': page_object,
               'current_page': current_page,
               'prev_page_url': prev_page,
               'next_page_url': next_page,
               'pages_count': pages_count}

    return render(request, 'films_finder/index.html', context)
