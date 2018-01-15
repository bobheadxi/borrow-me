# borrow-me (NWHacks 2018)

*Please borrow me!*

An AirBNB-style service for all the small everyday things you might need in life - pencils, erasers, chargers, phones, etc.

No money is involved: lending items and returning things on time allows you accumulate karma, which is the currency of Borrow Me.

## Design
The service is built on Django and uses a Postgres database, both of which are managed by Docker for deployment. It features user logins and accounts, and the front end has a feed for available items as well as account management features that allow you to see what items you are borrowing, when they are due, as well as check what items you have put listed as available.

## Development
The only things you need installed is Docker and the docker-compose tool. Then you can run:

```
docker-compose up --build
```

You can then visit the website at `0.0.0.0:8000`! Any changes you make to the general codebase should automatically be reflected.

When changes have been made to the database and/or models, you must completely remove the database container before attempting a build:

```
docker-compose rm -v db
```

To create a superuser:
```
docker-compose exec server bash
root@e3411fda73b7:/server# python manage.py createsuperuser
```
