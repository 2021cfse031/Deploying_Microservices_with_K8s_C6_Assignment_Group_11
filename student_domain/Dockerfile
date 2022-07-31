FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code
ADD requirements.txt /code/
RUN pip install -r /code/requirements.txt
COPY . ./
EXPOSE 7000