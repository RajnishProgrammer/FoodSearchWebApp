FROM python:3.9

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the port for the Django development server
EXPOSE 8000

# Set the command to start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
