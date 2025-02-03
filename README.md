# FastAPI - TaskManager

Этот тест-проект представляет собой веб-приложение для управления задачами, разработанное с помощью фреймворка FastApi. Позволяет организовывать и управлять задачами. 
## Предварительные требования и технологии проекта
![](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)
![](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

  * Python 3.11 (не ниже) 
  * Fast-Api
  * Docker
  * SQLAlchemy (для работы с бд и управлением моделями)
  * Pydantic (для работы с моделями запросов и ответов)

## Установка и запуск
1. Клонировать репозиторий на локальный компьютер
```python
git clone https://github.com/rburym/FastApiProject-TaskManager.git
```

2. Установить необходимые библиотеки
```python
pip install -r requirements.txt
```

3. Docker
```
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Создание образа приложения
```
docker build . --tag fastapi_app
```
Запуск образа в контейнере с пробросом портов для доступа к контейнеру из интернета
```
docker run -p 80:80 fastapi_app
```

4. Запустить приложение
```python
python main.py
```

В тестовом веб-окружении достаточно перейти на http://127.0.0.1:8000/docs#/

## Лицензия
Этот проект лицензируется по лицензии MIT, см. файл LICENSE.md
для получения дополнительной информации.

## Над проектом работали
Бурым Р.А.