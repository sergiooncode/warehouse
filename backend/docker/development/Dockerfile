FROM warehouse-backend-base

COPY . /warehouse-backend

WORKDIR /warehouse-backend

COPY ./docker/uwsgi.ini /etc/uwsgi/conf.d/uwsgi.ini

CMD ["uwsgi", "--ini", "/etc/uwsgi/conf.d/uwsgi.ini"]
