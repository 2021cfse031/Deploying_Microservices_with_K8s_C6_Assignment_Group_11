FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code_2
WORKDIR /code_2
ADD . /code_2
ADD requirements.txt /code_2/
RUN pip install -r /code_2/requirements.txt
COPY . ./
EXPOSE 9000