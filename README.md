# borrow-me
## NWHacks 2018
Please borrow me!

## Development
```
docker-compose up --build
```
The `--build` argument is not necessary if you have not made major changes to the app.

Then:
```
docker-compose exec server bash
root@e3411fda73b7:/server# python manage.py createsuperuser
```
