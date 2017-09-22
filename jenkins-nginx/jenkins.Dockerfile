from jenkins:alpine
MAINTAINER clemenko@docker.com
LABEL RUN="docker run -d -v /var/run/docker.sock:/var/run/docker.sock -v /jenkins/:/var/jenkins_home -v /jenkins/.ssh:/root/.ssh/ -p 8080:8080 -p 50000:50000 --name jenkins superjenkins"
USER root
RUN apk -U --no-cache add docker
