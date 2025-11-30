# Roadsafe_agent

Automated Pothole Detection & Reporting Multi-Agent System.

This repository contains a modular, easy-to-run implementation of the RoadSafe Agent pipeline:
- DetectionAgent (mock by default; plug Gemini Vision or other detector)
- SeverityAgent
- LocationAgent (mock reverse-geocode; can use Google Maps API)
- ReportAgent (produces JSON + PDF)
- MemoryBank (JSON-backed)

Run locally or in Kaggle. No API keys required for the default mock workflow.
🧠 Core Features
🔍 Autonomous Pothole Detector Agent

The main agent receives an image, analyzes road surfaces, and determines:

Whether a pothole is present

Severity level

Bounding-box region (approximate)

Confidence score

Explanation of visual cues

🧰 Custom Tools

Tools are implemented to handle:

Image loading

Image preprocessing

Running detection logic

Visualization support

Saving structured output

💾 Memory

The system uses a memory backend (memory/) so the agent can:

Recall previous interactions

Improve reasoning consistency

Reduce hallucinations

🧪 Tests

The tests/ folder contains example images and test scripts that verify:

Tool function correctness

Agent decision workflow

End-to-end pothole detection

## Quickstart (local)

1. Create and activate a Python venv (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run an example:
   ```bash
   python agents/main_runner.py --image tests/example_pothole.jpg --lat 28.7031 --lon 77.0219 --user_id test_user
   ```
   if any other image change the name of example_pothole.jpg to that image name

Outputs will be saved under `outputs/`.

4.## Environment Setup
Create a `.env` file in the project root with your own API keys:

GOOGLE_API_KEY=your_key_here
MAPS_API_KEY=your_key_here


