 FROM python:3
 RUN mkdir /backend
 ADD requirements.txt /backend/
 WORKDIR /backend
 RUN pip install  -r requirements.txt
 ADD . /backend/
 EXPOSE 8000
 
 # Copy wait-for-it.sh into our image
COPY wait-for-it.sh wait-for-it.sh
# Make it executable, in Linux
RUN chmod +x wait-for-it.sh
 #COmando i para iniciar el back luego de testear conexion a la bd 
 CMD ["./wait-for-it.sh", "db:5432", "--","python", "manage.py", "runserver", "0.0.0.0:8000"] 
 