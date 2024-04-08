#!/usr/bin/node
const { argv } = require('process');

if (argv.length <= 2 || isNaN(parseInt(argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  const times = parseInt(argv[2]);
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
