"""
BizShake PoC Smart Contract for Neo

Giuseppe Lo Presti @glpatcern

"""

import bzsstorage

RENT = 'RENT'

class SmartRent:

	def __init__(self, store, operation, args):
		self.store = store
		self.op = operation
		self.args = args

	def execute(self):
		try:
			if self.op == 'NewDeal':
				dealData = {
					'lessorWallet': self.args[0],
					'category': self.args[1],
					'description': self.args[2],
					'rentFee': self.args[3],
#					'deposit': self.args[4],
				}
				id = self.store.put(RENT, dealData)
				print(id)
				return id

			if self.op == 'GetDeal':
				dealData = self.store.get(RENT, self.args[1])
				print(dealData)
				return dealData

			if self.op == 'ListDeals':
				# TODO missing impl
				currDeals = self.store.list(RENT)
				print(currDeals)
				return True

			if self.op == 'DeleteDeal':
				# TODO check API for failures
				self.store.delete(RENT, self.args[1])
				return True

		except Exception as e:
			import sys
			ex_type, ex_value, ex_traceback = sys.exc_info()
			print(ex_traceback)

		finally:
			return False
