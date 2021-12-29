// SPDX-License-Identifier: MIT
// Created by NTFSWAP Team

pragma solidity ^0.6.12;

contract X {}
contract A is X {}
contract C is X, A {}