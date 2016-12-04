FROM olajir/projbase1:latest

WORKDIR /tmp
COPY . /tmp

RUN pip install --no-cache-dir .

RUN rm -r *

RUN mkdir -p /usr/src/app

COPY ./app/ /usr/src/app

WORKDIR /usr/src/app

CMD python ./app.py
