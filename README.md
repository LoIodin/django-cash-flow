# Веб-сервис для управления движением денежных средств 

Разработано веб-приложение, которое позволяет пользователям создавать, редактировать, удалять и просматривать записи о движении денежных средств.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git init
   git clone https://github.com/LoIodin/django-cash-flow
   cd django-cash-flow
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   venv\Scripts\activate     
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Подготовка базы данных

1. Выполните миграции:
   ```bash
   python manage.py migrate
   ```

2. Создайте суперпользователя для доступа к административной панели:
   ```bash
   python manage.py createsuperuser
   ```

## Запуск сервера разработки

Запустите сервер разработки с помощью команды:
```bash
python manage.py runserver
```

Перейдите в браузере по адресу [http://localhost:8000/](http://localhost:8000/), чтобы увидеть главную страницу приложения.

Административная панель доступна по адресу [http://localhost:8000/admin/](http://localhost:8000/admin). Используйте учетные данные суперпользователя для входа.

Документация API доступна по адресу [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/).

