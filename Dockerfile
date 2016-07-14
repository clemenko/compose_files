FROM alpine
RUN apk -U upgrade && apk add python &&\
    apk add py-pip py-mysqldb &&\
    pip install --upgrade pip &&\
    pip install flask redis Flask-MySQL &&\
    rm -rf /var/cache/apk/*
WORKDIR /code
ADD . /code
EXPOSE 5000
CMD ["python", "app.py"]
