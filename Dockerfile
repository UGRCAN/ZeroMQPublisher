# Dockerfile, Image, Container
FROM python:3.7.1

ADD pub.py .

RUN pip install zmq

CMD [ "python", "./pub.py"]