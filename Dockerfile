# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /usr/bin/inception_service
WORKDIR /usr/bin/inception_service

# Copy the current directory contents into the container at /app
COPY . /usr/bin/inception_service

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "inception_service.py"]
