# Базовый образ Python
FROM python:3.10-slim-bullseye

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Запуск как пакет (корректно для импорта внутри app)
CMD ["python", "-m", "app.main"]
