release: flask db migrate --directory app/migrations && flask db upgrade --directory app/migrations
web: gunicorn app.wsgi:app