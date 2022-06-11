# api_yatube
Это api умеет:

- смотреть и создавать посты, редактирование и удаление доступно для автора
- смотреть и создавать комментарии, редактирование и удаление доступно для автора
- просмотр групп - как всех, так и отдельных
- подписаться на автора

### Как запустить проект:

#### Клонировать репозиторий и перейти в него в командной строке:

```
HTTPS: git clone https://github.com/Ho1yGun/api_final_yatube.git
SSH: git clone git@github.com:Ho1yGun/api_final_yatube.git
```

```
cd api_final_yatube
```

#### Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
или 
python -m venv env для windows, далее так же
```

```
source env/bin/activate
```

#### Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

#### Выполнить миграции:

```
python3 manage.py migrate
```

#### Запустить проект:

```
python3 manage.py runserver
```
### Эндпоинты:
```
/api/v1/posts/ - GET, POST
/api/v1/posts/{id}/- GET, PUT, PATH, DELETE
/api/v1/posts/{id}/comment - GET, POST
/api/v1/posts/{id}/comment/{id} - GET, PUT, PATH, DELETE
/api/v1/groups/ - GET
/api/v1/groups/{id} - GET
/api/v1/follow/ - GET, POST
/api/v1/jwt/create/ - POST
/api/v1/jwt/refresh/ - POST
/api/v1/jwt/verify/ - POST
```
```
Более подробную информацию с вариантами ответов можно посмотреть в /redoc
```

#### Автор проекта Ho1yGun, практическая работа Яндекс Практикум.