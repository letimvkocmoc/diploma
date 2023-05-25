# Указывает, что Докер будет использовать официальный образ Python 3.10 с DockerHub
FROM python:3.10-slim

# Устанавливает переменную окружения, которая гарантирует, что вывод из Python будет отправлен прям в терминал без предварительной буферизации
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

# Обновляет библитеки
RUN pip install --upgrade pip

# Копирует файл с зависимостями
ADD requirements.txt /usr/src/app/requirements.txt

# Установка зависимостей
RUN pip install -r /usr/src/app/requirements.txt

COPY . /usr/src/app

WORKDIR /usr/src/app/todolist

COPY . /usr/src/app/todolist

EXPOSE 8000

# Выполняет запуск сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

