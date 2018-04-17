"""
BizShake PoC Smart Contract for Neo

Giuseppe Lo Presti @glpatcern
"""

from boa.interop.Neo.Storage import GetContext, Put, Delete, Get
from boa.builtins import concat

"""Helper module to augment SC storage with a double key"""

def put(category, id, value):
	skey = concat(category, id)
	Put(GetContext(), skey, value)
		
def get(self, category, id):
	skey = concat(category, id)
	v = Get(GetContext(), skey)
	if v == 0:
		return None
	return v

def delete(self, category, id):
	skey = concat(category, id)
	return Delete(GetContext(), skey)
