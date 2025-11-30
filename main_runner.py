from dotenv import load_dotenv
load_dotenv()

import argparse, os
from agents.detection_agent import DetectionAgent
from agents.severity_agent import SeverityAgent
from agents.location_agent import LocationAgent
from agents.report_agent import ReportAgent
from memory.memory_bank import MemoryBank

def main(args):
    det = DetectionAgent()
    sev = SeverityAgent()
    loc = LocationAgent(api_key=os.getenv('GOOGLE_MAPS_API_KEY'))
    rep = ReportAgent(out_dir='outputs')
    mem = MemoryBank('memory/memory.json')

    detection = det.run(args.image)
    print('-- Detection output --')
    print(detection)
    if not detection.get('pothole_detected'):
        print('No pothole detected. Exiting.')
        return

    severity = sev.run(detection)
    print('-- Severity output --')
    print(severity)

    location = loc.run(args.lat, args.lon)
    print('-- Location output --')
    print(location)

    final = rep.run(detection, severity, location, args.user_id)
    mem.add_report(final['report'])
    print('Report generated:', final)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', required=True)
    parser.add_argument('--lat', type=float, required=True)
    parser.add_argument('--lon', type=float, required=True)
    parser.add_argument('--user_id', required=True)
    args = parser.parse_args()
    main(args)
