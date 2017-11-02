# compose-tf-ci

Originally thinking about mapping docker concepts to docker-compose. 
First, googling stackoverflow.
In the end, the solution is actually in official document, not anywhere else.

I think I found out by googling "docker compose, docker run, corresponding".

I saw "As with docker run , options specified in the Dockerfile (e.g., CMD , EXPOSE , VOLUME ....." in the Google result page. 

And I think maybe there is clue for me to specify somethin like Dockerfile CMD in docker-compose yml file just when I am giving up.


https://docs.docker.com/compose/compose-file/#compose-file-structure-and-examples
https://stackoverflow.com/questions/29835905/docker-compose-using-multiple-dockerfiles-for-multiple-services

https://stackoverflow.com/questions/41299514/docker-compose-define-mount-for-bind-mount-and-managed-mount
quote the above s.o.f. post:
I'm using docker-compose for defining my service. In docker, there are two concepts for docker volume. Firstly is about bind mount: mount on host storage.

docker run -d --name web-app -v $HOST/location:/container/location -p 80:80 httpd:latest
Secondly is about managed mount: abstract storage, not depend on host.

docker run -d --name web-app -v /container/location -p 80:80 httpd:latest
I want to map those concepts to docker-compose. It means how can I define bind mount and managed mount when using docker-compose.

