
from platform_sdk.utils.http import HttpClient


class DomainReaderApi:
    def __init__(self, params):
        self.base_uri = params['api_url']
        self.client = HttpClient()

    def get_entities(self, app_name, map_name,filter_name, _params):
        uri = self._mount_uri(app_name, map_name,filter_name, _params)
        print(uri)
        return self.client.get(uri)

    def _mount_uri(self, app_name, map_name,filter_name, _params):
        return '{}{}/{}/{}?{}'.format(self.base_uri, app_name, map_name,filter_name, _params)