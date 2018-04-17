"""
BizShake PoC Smart Contract for Neo

Giuseppe Lo Presti @glpatcern

"""

RENT = 'RENT'

class SmartRent:

	def __init__(self, store):
		self.store = store

	def execute(self, op, args):
		if op == 'NewAsset':
			self.store.put(RENT, args[1], args[2])
			return True

		if op == 'GetAsset':
			assetData = self.store.get(RENT, args[1])
			print(assetData)
			return assetData != None

		if op == 'DeleteAsset':
			# TODO check API for failures
			self.store.delete(RENT, args[1])
			return True

		return False
