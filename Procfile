init: flask db init --directory app/migrations
migrate: cd app && flask db migrate
upgrade: flask db upgrade
web: gunicorn app.wsgi:app