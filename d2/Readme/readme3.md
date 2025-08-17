Как установить Docker на Ubuntu:
1. Обнови список пакетов:
    sudo apt update
2. Установи Docker:
    sudo apt install docker.io
3. Проверяй успешность установки:
    docker --version

Проблемы с установко на Ubuntu
Похоже, что у тебя проблема с репозиториями Ubuntu. Это сообщение говорит о том, что система не смогла найти пакет docker.io. Скорее всего, нужные репозитории не включены или возникли временные сетевые проблемы.

Давай исправим ситуацию:

Пошаговая проверка и решение:
1. Обновление списка пакетов:Сначала убедимся, что база данных пакетов обновлена:
    sudo apt update
2. Установка необходимого программного обеспечения для поддержки HTTPS и добавления ключей безопасности:Возможно, необходимы некоторые утилиты для правильной обработки репозиториев:
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
3. Добавляем ключ репозитория Docker:Нужно добавить открытый ключ для проверки подлинности пакета Docker:
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
4. Настройка стабильного репозитория Docker:Затем добавляем сам репозиторий Docker в список источников APT:
    echo \
    "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
5. Обновляем базу данных повторно:Повторяем обновление базы данных:
    sudo apt update
6. Устанавливаем Docker CE (Community Edition):Наконец, устанавливаем Docker Community Edition:
    sudo apt install docker-ce docker-ce-cli containerd.io
7. Проверка установки:Посмотри статус службы Docker и проверяй версию:
    sudo systemctl status docker
    docker --version
