"""
BizShake PoC Smart Contract for Neo

Giuseppe Lo Presti @glpatcern

"""

from boa.interop.Neo.Runtime import GetTrigger, CheckWitness
#from boa.interop.Neo.TriggerType import Application, Verification
import bzsstorage
from smartrent import SmartRent
from smartpawn import SmartPawn

ctx = GetContext()
rentDealOps = ['NewDeal', 'ListDeals', 'GetDeal', 'DeleteDeal', 'PreLock', 'ExecuteDeal']
pawnDealOps = []

def Main(operation, args):
    """

    :param operation: str The name of the operation to perform
    :param args: list A list of arguments along with the operation
    """

    # Am I who I say I am?
    user_hash = args[0]
    authorized = CheckWitness(user_hash)
    if not authorized:
        print("Not Authorized")
        return False
    print("Authorized")

    # initialize custom storage
    store = bzsstorage.BzsStorage()

    # dispatch
    if operation in rentDealOps:
        print("SmartRent operation")
        return SmartRent(store).execute(operation, args)

    if operation in pawnDealOps:
        print("SmartPawn operation")
        return SmartPawn(store).execute(operation, args)

    return False
