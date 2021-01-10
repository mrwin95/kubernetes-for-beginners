FROM python:3.8-alpine

WORKDIR /app

# Install our requirements

ADD requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

#Copy our code from the current folder to /app inside container

ADD . /app

# Make port 80 available

EXPOSE 80

# Define our command to be run when launch container

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80", "--log-file", "-", "--workers", "4", "--keep-alive", "0"]
