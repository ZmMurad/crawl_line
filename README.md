# crawl_line
#pet-project
## Установка и запуск 1 способ

1. Склонировать репозиторий с Github
2. Перейти в директорию проекта
3. Запустить контейнеры
```
sudo docker-compose up -d
```
4. Остановка работы контейнеров
```
sudo docker-compose stop
```
***
## Установка и запуск 2 способ
1. Склонировать репозиторий с Github
2. Перейти в директорию проекта
3. Запустить
```
pip install -r requirements.txt
```
4. Запустить
```
python manage.py runserver 0.0.0.0:8000
```