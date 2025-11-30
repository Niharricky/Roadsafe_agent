import os
import subprocess

IMAGE_FOLDER = "tests"
LAT = "28.7041"
LON = "77.1025"
USER_ID = "12345"

for filename in os.listdir(IMAGE_FOLDER):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(IMAGE_FOLDER, filename)
        print(f"Processing {image_path}")
        subprocess.run([
            "python", "main_runner.py",
            "--image", image_path,
            "--lat", LAT,
            "--lon", LON,
            "--user_id", USER_ID
        ])
