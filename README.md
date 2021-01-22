# Cargo Market Portal
The cargo market portal allows companies to send their cargo to their customers quickly. For drivers, it allows them to find a delivery job quickly.

# Installation
```
python3.7 -m venv venv3
Linux   : source venv3/bin/activate
Windows : ./venv3/bin/Scripts/activate
pip3 install -r requirements.txt
```

# Requirements
- django
- django-extensions
- django-widget-tweaks
- channels
- channels_redis
- ipython (dev purposes)

# Database Migrations
If you want to delete the existing DB and migration scripts, please use `delete_db` command in `Scripts` section.
```
./manage.py makemigrations account
./manage.py migrate
```

# Runserver
Please visit `127.0.0.1:8000/` after the below command.
```
./manage.py runserver
```

# Scripts
| Command | Usage | Description |
|:-------|:-----|:------------|
| init_db | `./manage.py runscript init_db` | Allows you to create dummy data. Applys migrations also. If you start a new app, please insert the app name to script. |
| delete_db | `./manage.py runscript delete_db` | Allows you to delete DB and migrations from filesystem |

# Docker Run
Open a docker console for chat application with redis
```
docker run -p 6379:6379 redis:5
```
