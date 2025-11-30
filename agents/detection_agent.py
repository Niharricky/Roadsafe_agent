
import os
from PIL import Image
import hashlib

class DetectionAgent:
    def __init__(self, model_name=None):
      
        self.model_name = model_name or os.getenv('DETECTION_MODEL', 'mock')

    def _hash_image(self, path):
        with open(path, 'rb') as f:
            data = f.read()
        return hashlib.md5(data).hexdigest()

    def _mock_detection(self, path):
      
        img = Image.open(path).convert('RGB')
        w, h = img.size
        
        box = [int(w*0.25), int(h*0.55), int(w*0.7), int(h*0.86)]
        return {
            'pothole_detected': True,
            'boxes': [box],
            'confidence': 0.88,
            'image_hash': self._hash_image(path)
        }

    def _call_real_detector(self, path):
       
        raise NotImplementedError('Real detector not implemented. Use mock or implement _call_real_detector.')

    def run(self, image_path):
        if self.model_name == 'mock':
            return self._mock_detection(image_path)
        else:
            return self._call_real_detector(image_path)
