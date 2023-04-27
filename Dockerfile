FROM ubuntu:latest

WORKDIR /app

COPY app.py app.py

RUN apt-get update
RUN apt-get install -y fortune fortunes
RUN apt-get install -y cowsay
RUN apt-get install -y python3.10
RUN apt-get install -y python3-pip

ENV PATH=$PATH:/usr/games
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV PORT=5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
