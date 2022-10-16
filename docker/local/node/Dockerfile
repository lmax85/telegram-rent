# specify the node base image with your desired version node:<version>
FROM node:16
ENV APPDIR /nuxt-app
WORKDIR ${APPDIR}

RUN apt-get update && apt-get install bash

EXPOSE 4000

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=4000

COPY entrypoint.sh /tmp/entrypoint.sh
RUN chmod +x /tmp/entrypoint.sh

CMD ["/tmp/entrypoint.sh"]
