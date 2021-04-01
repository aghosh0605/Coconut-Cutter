# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v7/python:2.7.13-jessie

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
