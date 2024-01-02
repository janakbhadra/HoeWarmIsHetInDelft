## Description
This Python script fetches the current temperature from a specific website using Selenium and Chrome. It extracts the temperature value and prints it in both the original format and as an integer in degrees Celsius. Additionally, a Dockerfile is provided to containerize the application.

## Prerequisites
Python 3.x
Google Chrome installed
ChromeDriver (included in the project using chromedriver-py)

## Installation
  1. Clone the repository:
     ```bash
     git clone https://github.com/your-username/your-repository.git
     
  2. Build the Docker image:
     ```bash docker
     build -t your-image-name .

  4. Run the Docker container:
     ```bash
     docker run -p 80:80 your-image-name

## Usage
  The script Launches a headless Chrome browser, navigate to a specific website, and extract the current temperature. 
  If running locally without Docker:
  ```bash
  python your_script.py

#### Configuration
  No additional configuration is required. The script uses the default settings for ChromeDriver.

#### Docker Configuration
  The Dockerfile provided in the repository automates the setup of the required dependencies and runs the Python script within a Docker container.

#### Contributing
  If you would like to contribute to this project, feel free to open an issue or submit a pull request.

#### Acknowledgments
  Selenium - Web browser automation framework
  chromedriver-py - ChromeDriver binary package for Python

Feel free to customize the README file further based on your specific project details and needs. Additionally, update the placeholders like [Your Project Title], [your-username], and [your-repository] with your actual project details.





