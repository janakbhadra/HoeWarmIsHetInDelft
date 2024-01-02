## Description
This Python script fetches the current temperature from a specific website using Selenium and Chrome. It extracts the temperature value and prints it in both the original format and as an integer in degrees Celsius. Additionally, a Dockerfile is provided to containerize the application.

## Prerequisites
1. Python 3.x
2. Google Chrome installed
3. ChromeDriver (included in the project using chromedriver-py)

## Installation
  1. Clone the repository:
     ```bash
     git clone https://github.com/janakbhadra/HoeWarmIsHetInDelft.git
     
  2. Build the Docker image (If you want to test script local using docker desktop):
     ```bash docker
     build -t your-image-name .

  4. Run the Docker container:
     ```bash
     docker run -p 80:80 your-image-name

## Usage
  The script Launches a headless Chrome browser, navigate to a specific website, and extract the current temperature. 
  To Test Python Script on Local System:
  1. Install dependencies
      ```bash
      pip install selenium
      pip install chromedriver-py
      
  2. Run the Python script:
     ```bash
      python your_script.py


## Configuration
  No additional configuration is required. The script uses the default settings for ChromeDriver.

## Docker Configuration
  The Dockerfile provided in the repository automates the setup of the required dependencies and runs the Python script within a Docker container.

## GitHub Actions
  The project includes a GitHub Actions workflow for building, testing, and deploying the Docker image.

## Contributing
  If you would like to contribute to this project, feel free to open an issue or submit a pull request.

## Acknowledgments
  1. Selenium - Web browser automation framework
  2. chromedriver-py - ChromeDriver binary package for Python



