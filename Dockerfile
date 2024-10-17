# Use the official Python image as a base
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file (if you have one)
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port that your app runs on
EXPOSE 5000

# Define the command to run your app
CMD ["python", "app.py"]
