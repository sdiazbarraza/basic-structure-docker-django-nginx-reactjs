# Base structure project Docker + Nginx + Postresql + PgAdmin + Django

_This project has backend api container make with django , frontend container made wih reactjs and database container made with Postgresql_
### How to run

```
 docker-compose build
```
# Migrations 
_Login backend container_ 
```
docker-compose exec -it  projectdock_backend_1 bash
```
_Create migrations_
```
python manage.py makemigrations backend
```
_Apply migrations_
```
python manage.py migrate backend
```
_Rollback migrations_
```
python manage.py migrate backend zero
```
### Go to frontend
_In the browser_
```
localhost
```
### Go to pgAdmin
_In the browser to connect with database_
```
localhost:7355
```
