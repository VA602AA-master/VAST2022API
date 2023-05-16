# VAST Challenge 2022 API
This web application is a REST API for the VAST Challenge 2022. It is built using [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
The application can be run with Docker or with Python.
The application has no data. This means that you should create and configure an external PostgreSQL database and configure the application to use it.

## Configuration
To configure the application create a new ```.env``` file in the root directory of the project. For a list of all the required varibles see the ```sample.env``` file.


## Python and Uvicorn
To start the application with a Python environment, install all the necessary libraries:
```
conda install --file requirements.txt
```
Then start the application with Uvicorn:
```uvicorn main:app --reload```
To give access to external connections, add ```--host 0.0.0.0``` to the command. To support multiple calls define a pool of workers with the option ```--workers 4```. For example:
```
uvicorn main:app --reload --host 0.0.0.0 --workers 4
```

## Docker
The application can be run with Docker. To build the image run:
```
docker compose up
```