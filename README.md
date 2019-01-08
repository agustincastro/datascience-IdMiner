# IdMiner

IdMiner for Term Discovery

## To install dependencies using venv

Create a virtual environment called virtual_env unsing python 3 venv tool.

`apt-get install python3-venv`

`python3 -m venv vidminer`

Activate the virtual environment

`source ./vidminer/bin/activate`

Install project requirements.

`pip install -r requirements.txt`

## In order to create and run a docker image for distribution:

To build the image:

`docker build --tag my-python-app .`

To run the image as a container:

`docker run --name python-app -p 8050:8050 my-python-app`

App will be ran on localhost port 8050
