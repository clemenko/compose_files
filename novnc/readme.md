#Setup
novnc for docker!

##Be warned this runs as root.

##Deploy
`docker run --rm -it -p 6080:6080 -v /var/run/docker.sock:/var/run/docker.sock clemenko/novnc`
