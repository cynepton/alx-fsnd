# The base image containing python to use to build our application
FROM python:3.9.14-buster

# Define the working directory
WORKDIR /app

# Copy our application code into the image
COPY . /app

# COPY main.py /app/main.py

# Install python libraries
RUN pip install -r requirements.txt

EXPOSE 8080

# Run the application
CMD [ "gunicorn", "-b", ":8080", "main:APP" ]