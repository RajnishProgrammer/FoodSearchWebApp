# Use the official Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the port on which Gunicorn will listen
EXPOSE 8000

# Set the command to start Gunicorn
CMD ["gunicorn", "foodsearchapp.wsgi", "--bind", "0.0.0.0:8000"]
