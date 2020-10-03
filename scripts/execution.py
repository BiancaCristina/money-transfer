from brownie import *

def isDisableCpf(cpf):
    # Can be implemented using several API's 
    return True

def deployContract(owner, destination):
    sc = MoneyTransfer.deploy(destination.address, {'from': owner})
    return sc

def setContractBalance(sc, owner):
    initialTX = sc.deposit({'from': owner, 'value': owner.balance()})
    print('Transferência inicial do owner para o smart contract')
    initialTX.info()
    print('Saldo inicial do SC = {amount}'.format(amount=sc.balance()))

def executeWithdraw(sc, destination):
    withdrawTX = sc.withdraw({'from': destination})
    print('Transferência realizada do smart contract pra destination')
    withdrawTX.info()

def showFinalBalance(sc): 
    print('Final balance SC = {amount}'.format(amount=sc.balance()))

def main(): 
    ownerCpf = '608.635.160-09'
    owner = accounts[0]
    destination = accounts[1]
    sc = deployContract(owner, destination)
    setContractBalance(sc, owner)

    if isDisableCpf(ownerCpf):
        executeWithdraw(sc, destination)
        showFinalBalance(sc)