# VirusTotal File Scanner

A simple Flask web application that allows users to upload files for analysis using the [VirusTotal API](https://www.virustotal.com/). The application scans the uploaded file and provides a detailed report on its safety.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contact](#contact)

## Features

- Upload files for analysis
- Get detailed report including file name, size, hash, and analysis results
- Easy-to-use web interface

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

## Contact

Shreya Barnwal - shreyabarnwal292@gmail.com
GitHub: shreya292


