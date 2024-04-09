#!/usr/bin/node

let numberOfArgumentsPrinted = 0; // This variable will keep track of the count

exports.logMe = function (item) {
  console.log(`${numberOfArgumentsPrinted}: ${item}`);
  numberOfArgumentsPrinted++; // Increment the counter after printing
};
