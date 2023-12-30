# Use an official Python runtime as a parent image
FROM python:3.12.1

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install dependencies (including Selenium)
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update -y \
    && apt-get install -y unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Download and install ChromeDriver
RUN wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_win32.zip \
    && unzip chromedriver_win32.zip \
    && rm chromedriver_win32.zip \
    && mv chromedriver.exe /usr/local/bin/

# Run myscript.py when the container launches
CMD ["python", "HoeWarmIsHetInDelft.py"]


