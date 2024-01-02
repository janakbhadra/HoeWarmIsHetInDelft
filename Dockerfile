# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y wget unzip gnupg

# Download and install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/google-archive-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list

# Update package list
RUN apt-get update

# Install Chrome
RUN apt-get install -y google-chrome-stable

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt


# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME temperature

# Run script.py when the container launches
CMD ["python", "HoeWarmIsHetInDelft.py"]
