FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "agents/main_runner.py", "--image", "tests/example_pothole.jpg", "--lat", "28.7031", "--lon", "77.0219", "--user_id", "docker_user"]
