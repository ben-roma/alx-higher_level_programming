#!/usr/bin/node
const { argv } = require('process');
const num1 = parseInt(argv[2], 10);
const num2 = parseInt(argv[3], 10);
const add = (num1, num2) => num1 + num2;

console.log(add(num1, num2));
