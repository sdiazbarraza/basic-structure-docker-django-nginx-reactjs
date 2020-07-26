 FROM python:3
 RUN mkdir /backend
 ADD requirements.txt /backend/
 WORKDIR /backend
 RUN pip install --no-cache-dir -r requirements.txt
 ADD . /backend/
 EXPOSE 8000
 #COmando para iniciar el back
 CMD  python manage.py runserver 0.0.0.0:8000