FROM python:3.8
WORKDIR /src
COPY  ./src/requirements.txt /src/
RUN pip install --upgrade pip && pip install -r requirements.txt 