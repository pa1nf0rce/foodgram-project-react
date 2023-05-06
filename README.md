# Foodgram(продуктовый помощник)
![workflow](https://github.com/pa1nf0rce/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

## :books:Описание:
  Пользователи **Foodgram** могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать в формате .txt сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Для удобства навигации по сайту рецепты размечены тэгами

[Продуктовый помощник](http://130.193.42.70)

[Путь до API](http://130.193.42.70/api/)

[Документация API](http://130.193.42.70/api/docs/redoc.html)

## :satellite: Технологии: 
  - Python
  - Django
  - Django REST Framework
  - API REST
  - Gunicorn
  - Docker
  - Nginx
  - Яндекс.Облако(Ubuntu 20.04 LTS)
 
 ### Инструкция для разворачивания проекта на удаленном сервере:

- Склонируйте проект из репозитория:

```sh
$ git clone https://github.com/Mukhinart/foodgram-project-react.git
```

- Выполните вход на удаленный сервер

- Установите DOCKER на сервер:
```sh
apt install docker.io 
```

- Установитe docker-compose на сервер:
```sh
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

- Отредактируйте конфигурацию сервера NGNIX:
```sh
Локально измените файл ..infra/nginx.conf - замените данные в строке server_name на IP-адрес удаленного сервера
```

- Скопируйте файлы docker-compose.yml и nginx.conf из директории ../infra/ на удаленный сервер:
```sh
scp docker-compose.yml <username>@<host>:~
scp nginx.conf <username>@<host>:~
```
- Создайте переменные окружения (указаны в файле ../infra/env.example) и добавьте их в Secrets GitHub Actions

- Установите и активируйте виртуальное окружение (для Windows):

```sh
python -m venv venv 
source venv/Scripts/activate
python -m pip install --upgrade pip
``` 

- Запустите приложение в контейнерах:

```sh
sudo docker-compose up -d --build
```

- Выполните миграции:

```sh
sudo docker-compose exec backend python manage.py migrate
```

- Создайте суперпользователя:

```sh
sudo docker-compose exec backend python manage.py createsuperuser
```

### Для запуска на локальной машине:

- Склонируйте проект из репозитория:

```sh
$ git clone https://github.com/Mukhinart/foodgram-project-react.git
```

- В папке ../infra/ переименуйте файл example.env в .env и заполните своими данными:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=<...> # секретный ключ django-проекта из settings.py
```

- Создайте и запустите контейнеры Docker (по инструкции выше).

После запуска проект будут доступен по адресу: [http://localhost/](http://localhost/)

Документация будет доступна по адресу: [http://localhost/api/docs/](http://localhost/api/docs/)

### Особенности заполнения данными:

- Добавьте теги для для рецептов через админ-панель проекта [http://localhost/admin/](http://localhost/admin/), т.к. это поле является обязательным для сохранения рецепта и добавляется только админом.

***

## :office_worker: Об авторах: 
[Авраменко Роман](https://github.com/pa1nf0rce),

