"""
BizShake PoC Smart Contract for Neo

Giuseppe Lo Presti @glpatcern

"""

from boa.interop.Neo.Runtime import CheckWitness, Log, Notify
#from boa.interop.Neo.TriggerType import Application, Verification
from boa.interop.Neo.Storage import GetContext, Put, Delete, Get
from boa.builtins import concat
#from smartrent import SmartRent
#from smartpawn import SmartPawn

rentOps = ['NewAsset', 'GetAsset', 'DeleteAsset']
pawnOps = []


"""Helper functions to augment SC storage with a double key"""

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


def Main(operation, args):
    """
    :param operation: str The name of the operation to perform
    :param args: list A list of arguments along with the operation
    """

    # Am I who I say I am?
    user_hash = args[0]
    authorized = CheckWitness(user_hash)
    if not authorized:
        Log("Not Authorized")
        return 'Not Authorized'

    # dispatch
    key = args[1]
    if operation == 'NewAsset':
        put('ASSET', key, args[2])
        output = concat("PutAsset stored ", args[2])
        print(output)
        return 'OK'

    if operation == 'GetAsset':
        assetData = get('ASSET', key)
        output = concat("GetAsset got ", assetData)
        print(output)
        return assetData

    if operation == 'DeleteAsset':
        res = delete('ASSET', key)
        output = concat("DeleteAsset got ", res)
        print(output)
        return res

#    if operation in pawnOps:
#        print("SmartPawn operation")
#        sp = SmartPawn(store)
#        return sp.execute(operation, args)

    return 'Invalid operation'
