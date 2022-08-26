# If you have docker and docker compose installed
1. Go to the project's root directory where you can see the docker-compose.yml file
2. Run the command `docker compose up --build -d` to run the application insde a docker container
3. And that's it! You'll see the server running after all images have been downloaded and the containers are running
4. To run tests, use the command `docker compose exec app pytest`
5. Note that in older versions of docker, you may need to use `docker-compose` in stead of `docker compose`

# If you have poetry installed in your system
1. Go to the project's root directory where you can see the pyproject.toml file
2. Run the command `poetry install` to install the dependencies
3. Run the command `poetry shell` to spawn the python virtualenv shell
4. Run `python src/main.py` to run the codebase
5. To run tests, use the command `pytest`

# If you want to use virtualenv
1. Go to the project's root directory where you can see the requirements.txt file
2. Install your virtualenv using `python3.9 -m virtualenv venv`
3. Run the command `source venv/bin/activate` to spawn the python virtualenv shell
4. Run the command `pip install -r requirements.txt` to install the dependencies
5. Run `python src/main.py` to run the codebase
6. To run tests, use the command `pytest`
