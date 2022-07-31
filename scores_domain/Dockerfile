FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code_1
WORKDIR /code_1
ADD . /code_1
ADD requirements.txt /code_1/
RUN pip install -r /code_1/requirements.txt
COPY . ./
EXPOSE 8000