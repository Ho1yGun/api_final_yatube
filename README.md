# api_yatube
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
