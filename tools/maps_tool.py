"""MapsTool: small wrapper for Google Maps Geocoding API (reverse)."""
import os, requests

class MapsTool:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('GOOGLE_MAPS_API_KEY')
        if not self.api_key:
            raise ValueError('GOOGLE_MAPS_API_KEY not set')

    def reverse_geocode(self, lat, lon):
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {'latlng': f'{lat},{lon}', 'key': self.api_key}
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        if data.get('results'):
            top = data['results'][0]
            return {'address': top.get('formatted_address'), 'place_id': top.get('place_id'), 'raw': top}
        return None
