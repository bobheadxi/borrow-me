echo "Hello world!"

echo "Waiting for Postgres to boot"
bash scripts/wait.sh "Postgres" "pg_isready -h db -p 5432"

python manage.py migrate
python manage.py runserver 0.0.0.0:8000