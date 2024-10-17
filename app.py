from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import sys
from time import sleep
import os

app = Flask(__name__)

# Function to simulate typing effect
def type(words: str):
    sleep(0.015)  # Adjust the sleep time to speed up/slower typing effect
    return words

# VirusTotal API and URL
url = r'https://www.virustotal.com/vtapi/v2/file/scan'
api = open("vt-api.txt", "r").read().strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file
        uploaded_file = request.files['file']
        if uploaded_file.filename == '':
            return "No file selected"
        
        # Save the uploaded file temporarily
        file_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(file_path)

        params = {"apikey": api}
        files = {"file": open(file_path, "rb")}

        # Make the POST request to upload the file
        response = requests.post(url, files=files, params=params)
        response_json = response.json()

        # Error handling for response
        if 'sha1' in response_json:
            file_url = f"https://www.virustotal.com/api/v3/files/{response_json['sha1']}"
        else:
            return "Error: Could not fetch file report."
        
        headers = {"accept": "application/json", "x-apikey": api}
        type("Analysing....")

        # Request the file report
        response = requests.get(file_url, headers=headers)

        # Check if the response is successful
        if response.status_code != 200:
            return f"Error: Failed to get report, status code {response.status_code}"

        # Load the response data into JSON
        report = json.loads(response.text)

        # Check if 'data' and 'attributes' exist in the report
        if "data" in report and "attributes" in report["data"]:
            name = report["data"]["attributes"].get("meaningful_name", "unable to fetch")
            hash = report["data"]["attributes"]["sha256"]
            descp = report["data"]["attributes"]["type_description"]
            size = report["data"]["attributes"]["size"] * 10**-3
            result = report["data"]["attributes"]["last_analysis_results"]
        else:
            return "Error: Invalid report structure."

        # Prepare analysis details
        analysis_details = {
            "name": name,
            "size": size,
            "description": descp,
            "hash": hash,
            "results": []
        }

        malicious_count = 0

        # Loop through analysis results
        for key, values in result.items():
            key_info = {'name': key, 'verdict': values['category']}
            
            if key_info['verdict'] == 'undetected':
                key_info['verdict'] = 'undetected'
            elif key_info['verdict'] == 'type-unsupported':
                key_info['verdict'] = 'type-unsupported'
            elif key_info['verdict'] == 'malicious':
                malicious_count += 1
                key_info['verdict'] = 'malicious'
            else:
                key_info['verdict'] = f'{key_info["verdict"]}'

            analysis_details["results"].append(key_info)

        # Summary based on malicious count
        analysis_details['malicious_count'] = malicious_count
        analysis_details['summary'] = (
            f"{malicious_count} antivirus found the given file malicious !!"
            if malicious_count != 0 else "No antivirus found the given file malicious !!"
        )

        return render_template('result.html', analysis_details=analysis_details)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
