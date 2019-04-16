import requests

from schema.command import *


class SchemaApi:
    url_schema_api = "http://localhost/schema/{0}/{1}/{2}"

    def get_schema(self, solution, app, _map):
        api_response = self._get_schema_response(solution, app, _map)
        api_response = api_response.json()
        model = api_response['model']
        fields = self._get_fields(api_response['fields'])
        filters = self._get_filter(api_response['filter'])
        return SelectCommand(model, fields, filters)

    def _get_schema_response(self, solution, app, _map):
        response = requests.get(self._get_schema_api_url(solution, app, _map))
        if response.ok:
            return response

    def _get_schema_api_url(self, solution, app, _map):
        return self.url_schema_api.format(solution, app, _map)

    def _get_filter(self, _filter):
        return Filter(_filter['name'], _filter['expression'])

    def _get_fields(self, fields):
        return [Field(f['name'], f['alias']) for f in fields]
