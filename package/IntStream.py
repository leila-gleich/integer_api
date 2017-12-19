import json
import requests

class IntStream:
    def __init__(self, api_key, leila1, leila2):
        #key as attribute to be reassigned if needed upon creation
        self.api_key = api_key
        self.leila1 = leila1
        self.leila2 = leila2
        self.stream = []
        self.response = {'last': 0, 'new': 0}

    def get_api_response(self, base_url):
        response = requests.get(
                            base_url,
                            headers = {
                            "x-api-key": self.api_key,
                            },
                            verify = True,  # Verify SSL certificate
                        )
        data = response.json()['data']
        return data

    def sort_responses(self):
        leila1_response = self.get_api_response(self.leila1)
        leila2_response = self.get_api_response(self.leila2)
        self.stream.append(leila1_response['next'])
        self.stream.append(leila2_response['next'])
        self.stream.sort()
        return self.stream

    def insert_values(self):
        self.sort_responses()
        self.response['last']=self.response['new']
        self.response['new']= self.stream.pop(0)
        return self.response
