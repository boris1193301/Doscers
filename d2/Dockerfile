# Используем базовый образ Python
FROM python:3.10-slim-bullseye

# Устанавливаем необходимые пакеты Python

COPY requirements.txt ./
RUN pip install -r requirements.txt

# Копируем приложение в рабочую директорию
WORKDIR /app
COPY app.py .

# Задаем команду для запуска
CMD ["python", "app.py"]
