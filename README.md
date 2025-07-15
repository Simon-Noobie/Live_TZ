
Live_TZ - Real-Time Timezone Dashboard (Django + Channels + Celery)

DESCRIPTION:
------------
Live_TZ is a real-time time zone dashboard built using Django. Users can register, select time zones, and view live time updates for each selected zone. The application uses Django Channels for WebSocket communication, Celery for background task scheduling, and Redis as a broker and channel layer backend.

FEATURES:
---------
- User registration, login, and logout.
- Selection of preferred time zones stored per user.
- Real-time updates of time every second via WebSockets.
- Background broadcasting of current time via Celery and Redis.
- WebSockets authenticated with Django sessions.

PROJECT DIRECTORY STRUCTURE:
----------------------------
Live_TZ/
├── manage.py
├── db.sqlite3
├── .gitignore
├── Live_TZ/
│   ├── asgi.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
└── main/
    ├── apps.py
    ├── admin.py
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    ├── consumers.py
    ├── routing.py
    ├── tasks.py
    ├── templates/
    │   └── main/
    │       ├── register.html
    │       ├── login.html
    │       └── timezones.html
    ├── migrations/
    └── __init__.py

TECHNOLOGIES USED:
------------------
- Python 3
- Django 5.x
- Django Channels
- Daphne (ASGI server)
- Celery with Celery Beat
- Redis (as broker and channel layer)
- pytz
- JavaScript (for WebSocket client)

WEBSOCKET IMPLEMENTATION:
-------------------------
- WebSocket URL: ws://<host>/ws/time/<timezone>/
- Defined in main/routing.py using Django Channels.
- Consumers (main/consumers.py) join channel layer groups named per timezone.
- Celery task broadcasts current time every second to these groups.
- Frontend JavaScript listens and updates the page live.

AUTHENTICATION:
---------------
- Django’s built-in auth system (login/logout/registration).
- AuthMiddlewareStack ensures WebSocket consumers are linked to authenticated users.
- Access control via @login_required in views.

SETUP & INSTALLATION:
---------------------
1. Clone the repository.
2. Install requirements (Django, channels, celery, redis, pytz).
3. Ensure Redis is running on localhost:6379.
4. Run migrations: python manage.py migrate
5. Start Celery: celery -A Live_TZ worker --beat --loglevel=info
6. Start Django server: python manage.py runserver OR use Daphne.
7. Visit /register/, create a user, log in, and go to the dashboard.

NOTES:
------
- Redis must be running for both Celery and Channels to work.
- Celery beat is used to run the broadcast task every second.
- Authentication is consistent across HTTP and WebSocket.

AUTHOR:
-------
Developed as part of an internship project.