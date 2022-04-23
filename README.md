# Название проекта job_flat

# Описание
## API для создания комментариев к публикациям с рекурсией и деревом комментариев
Возможности приложения:
- [X] Выдача списка всех публикаций.
- [X] Добавление новой публикации в коллекцию публикаций. 
- [X] Выдача публикации по id.
- [X] Обновление публикации по id. 
- [X] Частичное обновление публикации по id. 
- [X] Удаление публикации по id.
- [X] Выдача всех комментариев к публикации.
- [X] Добавление нового комментария к публикации.
- [X] Получение комментария к публикации по id.
- [X] Обновление комментария к публикации по id.
- [X] Частичное обновление комментария к публикации по id.
- [X] Удаление комментария к публикации по id.
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
## :books: Документация
Для того чтобы получить, описанные понятным языком эндпоинты и настройки, да ещё с примерами запросов, да ещё с образцами ответов!
Читай ReDoc, документация в этом формате доступна по ссылке:

```html
 http://127.0.0.1:8000/redoc/
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
