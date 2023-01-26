FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /web_build
WORKDIR /web_build
COPY requirements.txt /web_build/
RUN pip install -r requirements.txt
ADD . /web_build/