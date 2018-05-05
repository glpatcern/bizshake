from boa.blockchain.vm.Neo.Runtime import Log, Notify
from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.blockchain.vm.Neo.Transaction import *
from boa.blockchain.vm.Neo.Blockchain import GetHeight, GetHeader
from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.Neo.Runtime import GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
#from boa.blockchain.vm.Neo.Output import GetScriptHash, GetValue, GetAssetId
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete
#from boa.blockchain.vm.Neo.Header import GetTimestamp, GetNextConsensus

BZSVERSION = '0.5'

"""Helper functions to augment SC storage with a double key"""

def getversion():
    Log("Invoked GetVersion")
    return BZSVERSION

def put(category, id, value):
    skey = concat(category, id)
    Put(GetContext(), skey, value)
    
def get(category, id):
    skey = concat(category, id)
    v = Get(GetContext(), skey)
    if v == 0:
        return None
    return v

def delete(category, id):
    skey = concat(category, id)
    Delete(GetContext(), skey)


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
    ontid = args[0]
    authorized = CheckWitness(ontid)
    if not authorized:
        Log("Not Authorized")
        return 'Not Authorized'
    Log(ontid)

    # storage operations
    if operation == 'Store':
        if len(args) < 4:
            return 'Invalid arguments'
        category = args[1]
        id = args[2]
        value = args[3]
        put(category, id, value)
        #Notify(['Store:', category, id])
        return 'OK'

    if operation == 'Retrieve':
        if len(args) < 3:
            return 'Invalid arguments'
        category = args[1]
        id = args[2]
        data = get(category, id)
        #Notify(['Retrieve:', category, id])
        return data

    if operation == 'Delete':
        if len(args) < 3:
            return 'Invalid arguments'
        category = args[1]
        id = args[2]
        delete(category, id)
        #Notify(['Delete:', category, id])
        return 'OK'

    return 'Invalid operation'
