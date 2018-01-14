# borrow-me
## NWHacks 2018
Please borrow me!

## Development
```
docker-compose up --build
```

When changes have been made to the database and/or models, you must completely remove the database container before attempting a build:

```
docker-compose rm -v db
```

To create a superuser:
```
docker-compose exec server bash
root@e3411fda73b7:/server# python manage.py createsuperuser
```
