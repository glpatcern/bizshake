"""
BizShake PoC Smart Contract for Neo

Giuseppe Lo Presti @glpatcern

"""

import json
from uuid import UUID
from boa.interop.Neo.Storage import GetContext, Put, Delete, Get

class BzsStorage:
	"""Helper class to augment SC storage with a double key and handle JSON payloads"""

	def __init__(self):
		self.ctx = GetContext()

	def put(self, category, value):
		id = UUID.uuid4()
		Put(self.ctx, category + '/' + id, json.dumps(value))
		return id

	def get(self, category, id):
		v = Get(self.ctx, category + '/' + id)
		if v == 0:
			return None
		try:
			return json.loads(v)
		except ValueError:
			return v

	def list(self, category):
		# TODO
		return None

	def delete(self, category, id):
		return Delete(self.ctx, category + '/' + id)
