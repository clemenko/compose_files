FROM alpine
RUN apk -U upgrade && apk add python curl &&\
    apk add py-pip  &&\
    pip install --upgrade pip &&\
    pip install flask redis pymongo &&\
    rm -rf /var/cache/apk/*
WORKDIR /code
ADD . /code
EXPOSE 5000
HEALTHCHECK CMD curl -f http://localhost:5000/healthz || exit 1
CMD ["python", "app.py"]
