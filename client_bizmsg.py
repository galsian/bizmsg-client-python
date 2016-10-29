# -*- coding: utf-8 -*-
import requests
import json

API_URL = 'https://alimtalk-api.bizmsg.kr/v1/sender/send'
TEST_API_KEY = '40b1b96123c658aef539ba6b8b55aea6a98f7502'


class Bizmsg(object):
	def __init__(self, api_key, api_url = API_URL):
		self.api_key = api_key
		self.api_url = api_url
		requests_session = requests.Session()
		requests_adapters = requests.adapters.HTTPAdapter(max_retries=3)
		requests_session.mount('http://', requests_adapters)
		self.requests_session = requests_session

	def get_headers(self):
		return {'Content-type': 'Application/json'}

	def get_response(self, response):
		if response.status_code != requests.codes.ok:
			return {}
		result = response.json()
		return result

	def _post(self, url, payload):
		headers = self.get_headers()
		response = self.requests_session.post(url, headers=headers, data=json.dumps(payload))
		return self.get_response(response)

	def send_bizmsg(self, phone_number, msg, template_code):
		payload = [{
			"userId": "lifeengine",
			"message_type": "at",
			"phn": phone_number,
			"profile": self.api_key,
			"tmplId": template_code,
			"msg": msg	
		}]

		return self._post(url=API_URL, payload=payload)
