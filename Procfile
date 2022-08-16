init: flask db init --directory app/migrations
migrate: flask db migrate --directory app/migrations
upgrade: flask db upgrade --directory app/migrations
web: gunicorn app.wsgi:app