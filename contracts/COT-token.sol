pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";


contract COTToken is ERC20 {
    constructor(uint256 initialSupply) public ERC20("COTToken", "COT"){
        _mint(msg.sender, initialSupply);
    }
}