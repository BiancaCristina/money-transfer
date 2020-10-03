pragma solidity ^0.5.0;

contract MoneyTransfer {
    address owner;
    address destination; 

    constructor(address destinationAddress) public {
        owner = msg.sender;
        destination = destinationAddress;
    }

    modifier ifDestination() {
        if (destination != msg.sender) {
            revert();
        } else {
            _;
        }
    }

    function deposit() payable public {}

    function withdraw() public ifDestination {
        msg.sender.transfer(address(this).balance);
    }
}