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

storageOps = ['Store', 'Retrieve', 'Delete']
BZSVERSION = '0.4'

"""Helper functions to augment SC storage with a double key"""

def put(category, id, value):
    skey = concat(category, id)
    Put(GetContext(), skey, value)
    
def get(category, id):
    skey = concat(category, id)
    v = Get(GetContext(), skey)
    if v == 0:
        return None
    return v

# XXX Currently broken
def delete(category, id):
    skey = concat(category, id)
    Delete(GetContext(), skey)
    #Log(r)


def Main(operation, args):
    """
    :param operation: str The name of the operation to perform
    :param args: list A list of arguments along with the operation
    """

    if operation == 'GetVersion':
        # very simple method to test the contract
        Log("Invoked GetVersion")
        return BZSVERSION

    # Am I who I say I am? args[0] musth be the wallet hash code
    authorized = CheckWitness(args[0])
    if not authorized:
        Log("Not Authorized")
        return 'Not Authorized'
    Log(args[0])

    # storage operations
    if operation == 'Store':
        if len(args) < 4:
            return 'Invalid arguments'
        category = args[1]
        id = args[2]
        put(category, id, args[3])   # args[3] = arbitrary payload
        Notify(['Store:', category, id])
        return 'OK'

    if operation == 'Retrieve':
        if len(args) < 3:
            return 'Invalid arguments'
        category = args[1]
        id = args[2]
        skey = concat(category, id)
        data = Get(GetContext(), skey)
        #data = get(category, id)
        Notify(['Retrieve:', category, id])
        return data

    if operation == 'Delete':
        if len(args) < 3:
            return 'Invalid arguments'
        category = args[1]
        id = args[2]
        skey = concat(category, id)
        Delete(GetContext(), skey)
        Notify(['Delete:', category, id])
        return 'OK'

#    if operation in pawnOps:
#        print("SmartPawn operation")
#        sp = SmartPawn(store)
#        return sp.execute(operation, args)

    return 'Invalid operation'
