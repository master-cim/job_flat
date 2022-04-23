# Название проекта job_flat

# Описание
## API для создания комментариев к публикациям с рекурсией и деревом комментариев
Возможности приложения:
- [X] Выдача списка всех публикаций.
    - _При указании параметров limit и offset выдача  результата с пагинацией._
- [X] Добавление новой публикации в коллекцию публикаций. 
    - _Анонимные запросы запрещены._
- [X] Выдача публикации по id.
- [X] Обновление публикации по id. 
    - _Обновить публикацию может только автор публикации._
    - _Анонимные запросы запрещены._
- [X] Частичное обновление публикации по id. 
    - _Обновить публикацию может только автор публикации._
    - _Анонимные запросы запрещены._
- [X] Удаление публикации по id.
    - _Удалить публикацию может только автор публикации._
    - _Анонимные запросы запрещены._
- [X] Выдача всех комментариев к публикации.
- [X] Добавление нового комментария к публикации.
    - _Анонимные запросы запрещены._
- [X] Получение комментария к публикации по id.
- [X] Обновление комментария к публикации по id.
    - _Обновить комментарий может только автор комментария._
    -  _Анонимные запросы запрещены._
- [X] Частичное обновление комментария к публикации по id.
    - _Обновить комментарий может только автор комментария._
    - _Анонимные запросы запрещены._
- [X] Удаление комментария к публикации по id.
    - _Обновить комментарий может только автор комментария._
    - _Анонимные запросы запрещены._
- [X] Выдача списка доступных сообществ.
- [X] Выдача информации о сообществе по id.
- [X] Выдача всех подписок пользователя, сделавшего запрос.
    - _Анонимные запросы запрещены._
- [X] Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса.
    - _Анонимные запросы запрещены._
- [X] Выдача JWT-токена.
- [X] Обновление JWT-токена.
- [X] Проверка JWT-токена.[]
# Технологии в проекте
- [X] Django REST Framework
- [X] Python
# Инструкции по запуску
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/master-cim/job_flat.git
```

```
cd job_flat
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
. venv/Scripts/activate
```
Обновить версию pip
```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
# Примеры
:white_check_mark: Получение публикаций

```python
 `GET' /api/v1/posts/
```
:white_check_mark: Создание публикации
```Python
`POST' /api/v1/posts/
```
```
{
"text": "string",
"image": "string",
"group": 0
}
```
:white_check_mark: Получение, Обновление,  Частичное обновление, Удаление публикации по id.
```Python
`GET, PUT, PATCH, DELETE' /api/v1/posts/{id}/
```
```
{
"text": "string",
"image": "string",
"group": 0
}
```
:white_check_mark: Получение всех комментариев к публикации.
```Python
`GET' /api/v1/posts/{post_id}/comments/
```
:white_check_mark: Добавление нового комментария к публикации.
```Python
`POST' /api/v1/posts/{post_id}/comments/
```
```
{
"text": "string"
}
```
:white_check_mark: Получение, Обновление, Частичное обновление, Удаление  комментария к публикации по id.
```Python
`GET, POST, PATCH, DELETE' /api/v1/posts/{post_id}/comments/{id}/
```
```
{
"text": "string"
}
```
:white_check_mark: Получение списка доступных сообществ.
```Python
`GET' /api/v1/groups/
```
:white_check_mark: Получение информации о сообществе по id.
```Python
`GET' /api/v1/groups/{id}/
```
:white_check_mark: Получить Все подписки пользователя
```Python
`GET' /api/v1/follow/
```
:white_check_mark: Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса.
```Python
`POST' /api/v1/follow/
```
```
{
"following": "string"
}
```
:white_check_mark: Получение JWT-токена.
```Python
`POST' /api/v1/jwt/create/
```
```
{
"username": "string",
"password": "string"
}
```
:white_check_mark: Обновление JWT-токена.
```Python
`POST' /api/v1/jwt/refresh/
```
```
{
"refresh": "string"
}
```
:white_check_mark: Проверка JWT-токена.
```Python
`POST' /api/v1/jwt/verify/
```
```
{
"token": "string"
}
```
# Автор
### :small_orange_diamond: Светлана  Петрова _(Svetlana Yu. Petrova)_
```html
e-mail: master-cim@yandex.ru
```
```html
https://github.com/master-cim
```
![Svetlana Yu. Petrova](https://scontent-iev1-1.xx.fbcdn.net/v/t1.6435-9/p206x206/101204812_2968762206526462_4647695449438814208_n.jpg?_nc_cat=102&ccb=1-5&_nc_sid=da31f3&_nc_ohc=HlW3XVYBr3MAX8bhEGi&_nc_ht=scontent-iev1-1.xx&oh=00_AT-SmL9NzrKGJR1Omw4dt7rbXW-NNr_pcrXXOTM0V5fMuQ&oe=62086683 "Svetlana Yu. Petrova")
