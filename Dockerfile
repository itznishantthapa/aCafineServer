# Use the official Python image as the base image
FROM python:3.13.4

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install Python dependencies
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential pkg-config && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run database migrations and start the application
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
