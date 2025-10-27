# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your agent code into the container at /app
COPY . .

# Expose the port your agent will listen on (default for ADK web is 8080)
EXPOSE 8080

# Define environment variable for the ADK agent name
# Ensure this matches your agent's actual directory name
ENV ADK_AGENT_NAME="nexusagents"

# Command to run the ADK web server when the container starts
# The --port 8080 is crucial for Cloud Run to route traffic correctly
# --host 0.0.0.0 makes the server accessible from outside the container
CMD ["adk", "web", "--port", "8080", "--host", "0.0.0.0", "${ADK_AGENT_NAME}"]



















































