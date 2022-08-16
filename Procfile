init: flask db init --directory app/migrations
migrate: flask db migrate --directory app/migrations --package app
upgrade: flask db upgrade --directory app/migrations --package app
web: gunicorn app.wsgi:app