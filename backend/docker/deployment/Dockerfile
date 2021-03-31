FROM warehouse-backend-base

COPY ./backend /warehouse-backend

WORKDIR /warehouse-backend

COPY ./backend/docker/uwsgi.ini /etc/uwsgi/conf.d/uwsgi.ini

CMD ["uwsgi", "--ini", "/etc/uwsgi/conf.d/uwsgi.ini"]
