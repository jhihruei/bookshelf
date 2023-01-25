FROM python:3.10.6

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY ./backend/requirements.txt ./requirements.txt
RUN pip install --no-deps -r requirements.txt

COPY ./backend .
RUN make start
