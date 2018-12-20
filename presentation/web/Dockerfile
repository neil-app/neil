FROM node:8.11

WORKDIR /app
ADD . /app

ARG BUILD_ENV=local
ENV BUILD_ENV ${BUILD_ENV}

RUN npm install
RUN npm run build

ENV HOST 0.0.0.0
EXPOSE 3000

CMD ["npm", "run", "start"]
