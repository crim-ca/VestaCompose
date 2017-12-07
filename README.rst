Vesta compose recipe
====================

This is an example of a docker-compose recipe to assemble the `Vesta Services
Stack <http://vesta.crim.ca/docs/>`_. 

Most of the Docker images are meant to be public, if you cannot access the images,
please contact support-vesta@crim.ca . 


Overriding
----------

You can use a checked-out version of this repository to run a personalized
docker-compose for you testing or development needs. To do so, create a
docker-compose.override.yml file in which you will define new services, define
paths to your own configuration files and so on. See docker documentation at :
https://docs.docker.com/compose/extends/
