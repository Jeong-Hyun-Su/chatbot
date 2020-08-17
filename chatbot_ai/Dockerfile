FROM python:3.6
MAINTAINER mses1572 <mses1572@naver.com>
RUN apt-get -y update

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

COPY ./chatterbot_corpus /usr/local/lib/python3.6/site-packages/chatterbot_corpus

EXPOSE 5000
CMD ["python3","./server.py"]
