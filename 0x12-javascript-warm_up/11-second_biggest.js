#!/usr/bin/node
const { argv } = require('process');

if (argv.length <= 3) {
  console.log(0);
} else {
  const numbers = argv.slice(2).map(Number);
  const sortedNumbers = numbers.sort((a, b) => a - b).reverse();
  console.log(sortedNumbers[1]);
}
