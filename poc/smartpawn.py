"""
BizShake PoC Smart Contract for Neo

Giuseppe Lo Presti @glpatcern

"""

import bzsstorage

class SmartPawn:

	def __init__(self, store, operation, args):
		self.store = store
		self.op = operation
		self.args = args

	def execute(self):
		return False
