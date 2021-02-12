FROM python:3.9.1

WORKDIR /home/

RUN echo "testing"

RUN git clone https://www.github.com/bobyeong2/Fwings.git

WORKDIR /home/Fwings/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=8$i2q%3x*mcxg#ts-kfd^2p2hs))4ja5lo2e0_7x@2frsyh6eb" > .env

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash","-c","python manage.py migrate --settings=beginner.settings.deploy && gunicorn beginner.wsgi --env DJANGO_SETTINGS_MODULE=beginner.settings.deploy --bind 0.0.0.0:8000"]
