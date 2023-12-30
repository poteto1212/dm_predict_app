FROM python:3.7
WORKDIR /var/www/html
COPY  ./src/requirements.txt /var/www/html/
RUN pip install --upgrade pip && pip install -r requirements.txt 