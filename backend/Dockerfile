FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

#CMD ["sh", "-c", "python manage.py migrate; daphne -p 8000 backend.asgi:application; celery -A backend worker --loglevel=info"]
CMD ["sh", "-c", "python manage.py migrate; gunicorn backend.wsgi:application --bind 0.0.0.0:8000; daphne backend.asgi:application --port 8001 --bind 0.0.0.0"]
