FROM python:3.9

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Set the command to start the server
CMD gunicorn foodsearchapp.wsgi:application --bind 0.0.0.0:8080
