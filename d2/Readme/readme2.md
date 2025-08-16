Дополнительно:

Если у тебя много внешних библиотек, удобно создать отдельный файл требований (requirements.txt) и включить его в Dockerfile следующим образом:

...
COPY requirements.txt ./
RUN pip install -r requirements.txt
...

Получить файл requirements.txt из существующего виртуального окружения Python можно очень просто с помощью встроенного инструмента pip freeze.

1. Активируй своё виртуальное окружение (venv):
source venv/bin/activate

2. Генерируй файл requirements.txt:
    pip freeze > requirements.txt

