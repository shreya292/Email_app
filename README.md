# VirusTotal File Scanner

A simple Flask web application that allows users to upload files for analysis using the [VirusTotal API](https://www.virustotal.com/). The application scans the uploaded file and provides a detailed report on its safety.

## Table of Contents

- [Features](#features)
- [Prerequisities].(#prerequisites)
- [Requirements](#requirements)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Docker Setup].(#Docker-setup)
- [Contact](#contact)

## Features

- Upload files for analysis
- Get detailed report including file name, size, hash, and analysis results
- Easy-to-use web interface

## Prerequisites
- Docker: Ensure Docker is installed on your machine.
- Python: If you want to run it locally without Docker, make sure you have Python 3.10 or later installed.
- Flask: The Flask framework must be installed if running locally. You can install it via pip:
- pip install Flask requests

## Requirements

- Python 3.x
- Flask
- requests
- colorama

## Usage

- python app.py

## How It works

- The user uploads a file via the web interface.
- The application sends the file to the VirusTotal API for malware scanning.
- A detailed report is fetched from the VirusTotal API, which includes virus detection results from various antivirus engines.
- The report is displayed on the web page, showing file details such as size, hash, and analysis results.

## Docker Setup

- To pull the Docker image, run the following command: docker pull shreya1508/my-flask-app
- docker run -p 5000:5000 shreya1508/my-flask-app

## Contact

Shreya Barnwal - shreyabarnwal292@gmail.com
GitHub: shreya292

## Contribution

- prachiiBB
- shivanikumawat19
- Allampati-sireesha
- Sannapavithra
- TSathvik19


