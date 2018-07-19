#Setup

TLS Minio

Create a directory and copy the nginx.conf and jenkins-nginx.yml to it.
`mkdir -p guac/{certs,data}; chmod -R 777 guac; cd guac`

##Now create a cert : (change the IP)
`cd certs; openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/C=US/ST=MD/O=Docker/CN=206.189.198.251.xip.io"`

##init the swarm
`docker swarm init`

##Check the nonauth-config.xml to make sure the paths are correct.

##Check that the nginx.conf is located in the correct directory.

##Deploy the stack
`docker stack deploy -c guac.yml guac`
