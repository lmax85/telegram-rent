# specify the node base image with your desired version node:<version>
FROM node:16
ENV APPDIR /nuxt-app
WORKDIR ${APPDIR}

RUN apt-get update && apt-get install bash
COPY ./node-frontend ${APPDIR}
RUN npm ci --ignore-scripts
RUN npm run build

EXPOSE 4000

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=4000

CMD [ "npm", "start" ]
