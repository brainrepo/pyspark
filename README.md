# USE PYSPARK WITH PYSPARK-TEST

Installing pyspark on windows is annoying then this is a dockerized solution for running it.

## Steps

### Build the container

In order to start a docker container you should build it before,
here the command

**You need to rebuild the container when a new dep is included**

```
docker build . -t pyspark
```

This command says build the `Dockerfile` that is in the current directory and once built tag the resulting image `pyspark`

### Launch the environment and run the tests

To run the app you should run this command

```
docker run -v $(pwd):/job pyspark /job/src/test.py
```

if you want to run another file it is enough to create a new python file
in the folder (let's call it `new-file.py`) and run this command

```
docker run -v $(pwd):/job pyspark /job/new-file.py`
```

This command:

- make available the current directory to the docker container `-v $(pwd):/job` mapping it to the job folder:

```
HOST MACHINE (./src/index.py) -> DOCKER CONTAINER (/job/src/index.py)
```

- run the container passing the file we want to run `/job/new-file.py`

## Todo

- create a docker-compose file
