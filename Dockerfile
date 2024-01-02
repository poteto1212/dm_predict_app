FROM python:3.7
WORKDIR /src
COPY  ./src/requirements.txt /src/
RUN pip install --upgrade pip && pip install -r requirements.txt 