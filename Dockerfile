FROM alpine
RUN apk -U upgrade && apk add python &&\
    apk add py-pip  &&\
    pip install --upgrade pip &&\
    pip install flask redis pymongo &&\
    rm -rf /var/cache/apk/*
WORKDIR /code
ADD . /code
EXPOSE 5000
CMD ["python", "app.py"]
