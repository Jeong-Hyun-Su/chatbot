FROM node:12
MAINTAINER mses1572 <mses1572@naver.com>

COPY package*.json ./
RUN npm install --silent

COPY . /app
WORKDIR /app

EXPOSE 4000
CMD ["node","./server.js"]
