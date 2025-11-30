"""Simple JSON backed Memory Bank for storing reports."""
import json, os

class MemoryBank:
    def __init__(self, path='memory/memory.json'):
        self.path = path
        d = os.path.dirname(path)
        if d and not os.path.exists(d):
            os.makedirs(d, exist_ok=True)
        if not os.path.exists(path):
            with open(path, 'w') as f:
                json.dump({'reports': []}, f)

    def _load(self):
        with open(self.path, 'r') as f:
            return json.load(f)

    def _save(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=2)

    def add_report(self, report):
        data = self._load()
        data['reports'].append(report)
        self._save(data)

    def get_recent(self, n=10):
        data = self._load()
        return data['reports'][-n:]
