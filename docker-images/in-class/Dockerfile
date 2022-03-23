FROM ubuntu:latest

#always need to update. Need -y else it will ask for confirmation to install python3 and stall out.
RUN apt update && apt install -y python3 python3-pip
#RUN pip install python libraries

COPY . /project
# copy all contents of current directory (aka .) to /project inside the container

CMD ["python3", "/project/hello.py"]
# this is meant to run the .py script hello.py. hello.py needs to be in the same folder as Dockerfile so it can be used by the COPY . command
