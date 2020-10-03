# Money transfer using smart contracts

## Structure
The project follow Brownie structure, such as:

* /projects: developed contracts
* /interfaces: developed interfaces
* /scripts: scripts that allow interaction with the contracts
* /tests: scripts for tests
* /build: project data
* /reports: JSON reports

## Installation
### Prerequisites
* Brownie
* Ganache

Both can be installed following [this tutorial](https://medium.com/better-programming/part-1-brownie-smart-contracts-framework-for-ethereum-basics-5efc80205413).

### Project
To install the project, just clone it by using one of the following git commands:

**Using HTTP**:
```
git clone https://github.com/BiancaCristina/money-transfer.git
```

**Using SSH**:
```
git clone git@github.com:BiancaCristina/money-transfer.git
```

**Using GitHub CLI**:
```
gh repo clone BiancaCristina/money-transfer
```

## Local execution
Create an brownie network named "dev" (for Development environment) using:
```
brownie networks add Development dev host=http://127.0.0.1:7545 cmd=ganache-cli 
```

After that, compile the project and run the console with the following commands:
```
brownie compile
brownie console --network dev
```
**_NOTE:_**  to run brownie console successfully is necessary to have ganache running. 

Finally, with brownie console open, execute the script that interact with our contract using:
```python
run('execution')
```

For futher information about Ganache and Brownie, access respectively [Ganache documentation](https://www.trufflesuite.com/docs/ganache/quickstart) and [Brownie documentation](https://eth-brownie.readthedocs.io/en/stable/).