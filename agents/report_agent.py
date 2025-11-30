
import json, os, time, uuid
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

class ReportAgent:
    def __init__(self, out_dir='outputs'):
        self.out_dir = out_dir
        os.makedirs(self.out_dir, exist_ok=True)

    def _unique_suffix(self):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        random_id = uuid.uuid4().hex[:8]
        return f"{timestamp}_{random_id}"

    def _json_path(self, user_id):
        suffix = self._unique_suffix()
        return os.path.join(self.out_dir, f"report_{user_id}_{suffix}.json")

    def _pdf_path(self, user_id):
        suffix = self._unique_suffix()
        return os.path.join(self.out_dir, f"report_{user_id}_{suffix}.pdf")

    def _make_pdf(self, report, pdf_path):
        c = canvas.Canvas(pdf_path, pagesize=A4)
        width, height = A4
        c.setFont('Helvetica-Bold', 14)
        c.drawString(40, height - 60, 'RoadSafe — Pothole Report')
        c.setFont('Helvetica', 11)
        y = height - 90

        lines = [
            f"User ID: {report.get('user_id')}",
            f"Pothole detected: {report.get('pothole_detected')}",
            f"Confidence: {report.get('confidence')}",
            f"Severity: {report.get('severity', {}).get('label')}",
            f"Location: {report.get('location', {}).get('address')}",
            ''
        ]

        for line in lines:
            c.drawString(40, y, line)
            y -= 18

        c.save()

    def run(self, detection, severity, location, user_id):
        report = {
            'user_id': user_id,
            'pothole_detected': detection.get('pothole_detected'),
            'confidence': detection.get('confidence'),
            'boxes': detection.get('boxes'),
            'severity': severity,
            'location': location
        }

        # Generate unique file paths
        jpath = self._json_path(user_id)
        pdf_path = self._pdf_path(user_id)

        # Save JSON
        with open(jpath, 'w') as f:
            json.dump(report, f, indent=2)

        # Save PDF
        self._make_pdf(report, pdf_path)

        return {'json_path': jpath, 'pdf_path': pdf_path, 'report': report}
