
import os
try:
    from tools.maps_tool import MapsTool
except Exception:
    MapsTool = None

class LocationAgent:
    def __init__(self, api_key=None):
        self.maps = None
        key = api_key or os.getenv('GOOGLE_MAPS_API_KEY')
        if key and MapsTool:
            self.maps = MapsTool(api_key=key)

    def _mock_reverse_geocode(self, lat, lon):
        
        return {
            'address': f'Approximate location at ({lat:.5f}, {lon:.5f})',
            'ward': 'Ward 12',
            'place_id': None
        }

    def run(self, lat, lon):
        if self.maps:
            try:
                r = self.maps.reverse_geocode(lat, lon)
                
                address = r.get('address') if r else None
                return {'address': address, 'ward': None, 'raw': r}
            except Exception:
                return self._mock_reverse_geocode(lat, lon)
        else:
            return self._mock_reverse_geocode(lat, lon)
