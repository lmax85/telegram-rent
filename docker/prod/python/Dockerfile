FROM python:3

WORKDIR /app

RUN apt-get update && \
  apt-get upgrade && \
  apt-get -y install cron && \
  apt-get -y install bash && \
  apt-get -y install vim

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /tmp/entrypoint.sh
RUN chmod +x /tmp/entrypoint.sh

CMD ["/tmp/entrypoint.sh"]
# CMD [ "tail", "-f", "/dev/null" ]
