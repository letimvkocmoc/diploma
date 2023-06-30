# Указывает, что Докер будет использовать официальный образ Python 3.10 с DockerHub
FROM python:3.10-slim

# Устанавливает переменную окружения, которая гарантирует, что вывод из Python будет отправлен прям в терминал без предварительной буферизации
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

# Обновляет библитеки
RUN pip install --upgrade pip

WORKDIR /usr/src/app

# Копирует файл с зависимостями
ADD requirements.txt .

# Установка зависимостей
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# Выполняет запуск сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
