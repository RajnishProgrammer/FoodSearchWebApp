FROM python:3.9

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

# rest of the Dockerfile

# Set the base image
#FROM python:3.9-slim-buster

# Install system dependencies
#RUN apt-get update && apt-get install -y \
#    ffmpeg \
#    libsm6 \
#    libxext6

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Set the command to start the server
CMD ["python", "manage.py runserver"]
