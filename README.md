# API for social media 'Yatube'

### Технологии в проекте
- Python 3.7
- Django 2.2.19
- Django REST framework 3.12.4

### Как запустить проект:
- Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Tastybaev/api_final_yatube.git
```

- Cоздать и активировать виртуальное окружение:
```
python3 -m venv env

source env/bin/activate
```

- Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
``` 

- Выполнить миграции:
```
python3 manage.py migrate
```

-Запустить проект:
```
python3 manage.py runserver
```
## Примеры запроса

### GET

`GET /posts/`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/posts/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    [

    {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2021-08-24T14:15:22Z",
        "image": "string",
        "group": 0
    },
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2021-08-24T14:15:22Z",
        "image": "string",
        "group": 0
    },
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2021-08-24T14:15:22Z",
        "image": "string",
        "group": 0
    }

    ]

### GET ID

`GET /posts/<int:post_id>/`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/posts/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    [
        {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2021-08-24T14:15:22Z",
        "image": "string",
        "group": 0
        }
    ]
