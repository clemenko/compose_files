#Setup

TLS Minio

Create a directory and copy the nginx.conf and jenkins-nginx.yml to it.
`mkdir -p minio/{certs,data}; chmod -R 777 minio; cd minio`

##Now create a cert : (change the IP)
`cd certs; openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/C=US/ST=MD/O=Docker/CN=192.168.233.141.xip.io"`

##init the swarm
`docker swarm init`

##Check the minio.yml to make sure the paths are correct.

##Check that the nginx.conf is located in the correct directory. 

##Deploy the stack
`docker stack deploy -c minio.yml minio`
