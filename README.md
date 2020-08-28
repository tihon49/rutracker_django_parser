# Парсер фильмов с сайта [RuTracker.org](https://rutracker.org)

## Описание:
Приложение для сбора данных с сайта [RuTracker.org](https://rutracker.org), и более удобного отображения имеющихся там фильмов.

Вместо такой страницы:
![Иллюстрация к проекту](https://github.com/tihon49/rutracker_django_parser/blob/master/rutracker/images/raw.png)

Будет что-то в этом роде:<br>
![Иллюстрация к проекту](https://github.com/tihon49/rutracker_django_parser/blob/master/rutracker/images/good0.png)
<br><hr>
![Иллюстрация к проекту](https://github.com/tihon49/rutracker_django_parser/blob/master/rutracker/images/good1.png)
<br><hr>
![Иллюстрация к проекту](https://github.com/tihon49/rutracker_django_parser/blob/master/rutracker/images/good2.png)
<br><hr>
![Иллюстрация к проекту](https://github.com/tihon49/rutracker_django_parser/blob/master/rutracker/images/good3.png)
<hr>

## Инструкция
#### Прежде всего надо помнить что данный ресурс заблокирован на территории РФ, а это означает что нужно пользоватся VPN приложением.
* устанавливаем python по ссылке: [python](https://www.python.org/)

Тут можно посмотреть [подробное видео по установке](https://www.youtube.com/watch?v=LKVVtVVkj7Q).
* скачиваем данный репозиторий кликнув на зелененькую кнопку "Code", затем "Download ZIP"
* распаковываем скачанный архив
* открываем [командную строку](http://www.oszone.net/27750/windows10_cmd_admin)
* В командной строке перехрдим в папку **rutracker_django_parser**
далее в папку **rutracker** и пишем следующие команды:

установка необходимых библиотек:
```
pip install -r requirements.txt
```
делаем необходимые миграции:
```
python manage.py migrate
```
подгружаем наполнение БД по умолчанию (это не обязательно), после чего в базе данных уже будет стартовый набор фильмов и
админ панель с логином admin и паролем admin по адресу [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) :
```
python manage.py loaddata data.json
```
запускаем сервер на локальном хосте:
```
python manage.py runserver
```
После чего откройте браузер и перейдите по ссылке [127.0.0.1:8000](http://127.0.0.1:8000)
<hr>
Далее всё должно быть интуитивно понятно!<br>
Ниже можно посмотреть видеоинструкцию (нужно тыкнуть на изображение)
<hr>



[![Watch the video](https://img.youtube.com/vi/ZBt6vmN3vJA/0.jpg)](https://youtu.be/ZBt6vmN3vJA)
