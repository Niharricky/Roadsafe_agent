

class SeverityAgent:
    def __init__(self):
        pass

    def run(self, detection_output):
        conf = detection_output.get('confidence', 0.5)
        boxes = detection_output.get('boxes', [])
        if not boxes:
            return {'score': 0, 'label': 'None', 'explanation': 'No boxes'}

        box = boxes[0]
        try:
            x1, y1, x2, y2 = box
            area = max(0, (x2-x1) * (y2-y1))
        except Exception:
            area = 1000

        
        if conf > 0.9 or area > 150000:
            label = 'High'
            score = 5
        elif conf > 0.75 or area > 60000:
            label = 'Medium'
            score = 3
        else:
            label = 'Low'
            score = 1

        explanation = f'confidence={conf}, area={area}'
        return {'score': score, 'label': label, 'explanation': explanation}
