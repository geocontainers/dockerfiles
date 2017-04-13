# pycsw container

A docker image for [pycsw](http://pycsw.org/). It currently features version 2.0.2
This image has support for the following database backends:

- sqlite
- postgres


## How to use it

pycsw is configured by means of a configuration file. This image expects the
configuration file to be present at `/etc/pycsw/pycsw.cfg` by default (this can be overriden by
setting the `PYCSW_CONFIG` environment variable inside a container).

- Create a pycsw configuration file. Details regarding this file are available
  at http://docs.pycsw.org/en/2.0.2/configuration.html. pycsw's github
  repository provides a 
  [sample configuration](https://github.com/geopython/pycsw/blob/master/default-sample.cfg) 
  file to get you started. Pay special attention to the `repository:database`
  setting, which is where you can set the database backend parameters. When
  running a pycsw container, mount the configuration file in the expected
  location by using docker's `-v` option (see the examples for more details).

- Database backend initialization. There are two methods for initializing your
  backend:

  - Start a new pycsw container in order to get the pycsw server process 
    running. Then run the `pycsw-admin.py` command inside the container using
    `docker exec`;

  - Create a temporary container that takes care of initializing the backend.
    then create another container to run the already bootstrapped pycsw. This
    method only works if you use persistent data storage, such as sqlite with a
    docker volume or postgresql.


## Examples

Run a new container and initialize the backend with `docker exec` When the 
container is destroyed the data will be deleted too.

```
docker run \
    --rm \
    -ti \
    --name pycsw_test \
    -p 8000:8000 \
    -v <path_to_your_pycsw_config_file>:/etc/pycsw/pycsw-cfg \
    geocontainers/pycsw:2.0.2

docker exec -ti \
    pycsw_test pycsw-admin.py -f /etc/pycsw/pycsw.cfg -c setup_db
```


Create a new docker volume in order to persist the data. Setup a new sqlite 
database inside the volume by using a temporary container.

```
docker volume create pycsw_data

docker run \
    --rm \
    -ti \
    --name pycsw_test \
    -p 8000:8000 \
    -v <path_to_your_pycsw_config_file>:/etc/pycsw/pycsw-cfg \
    -v pycsw_data:/pycsw \
    geocontainers/pycsw:2.0.2 admin setup_db

# run pycsw
docker run \
    --rm \
    -ti \
    --name pycsw_test \
    -p 8000:8000 \
    -v <path_to_your_pycsw_config_file>:/etc/pycsw/pycsw-cfg \
    -v pycsw_data:/pycsw \
    geocontainers/pycsw:2.0.2
```


Create a new postgresql database and insert the relevant connection details
in the pycsw config file. Afterwards, initialize the database with a
temporary container and finally use another container to run pycsw

```
docker run \
    --rm \
    -ti \
    --name pycsw_test \
    -p 8000:8000 \
    -v <path_to_your_pycsw_config_file>:/etc/pycsw/pycsw-cfg \
    geocontainers/pycsw:2.0.2 admin setup_db

# run pycsw
docker run \
    --rm \
    -ti \
    --name pycsw_test \
    -p 8000:8000 \
    -v <path_to_your_pycsw_config_file>:/etc/pycsw/pycsw-cfg \
    geocontainers/pycsw:2.0.2
```
