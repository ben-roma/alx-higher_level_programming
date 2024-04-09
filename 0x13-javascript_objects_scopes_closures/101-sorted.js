#!/usr/bin/node

const { dict } = require('./101-data.js').dict;
console.log(dict);

const newDict = Object.entries(dict).reduce((acc, [userId, occurrence]) => {
  if (!acc[occurrence]) {
    acc[occurrence] = [];
  }
  acc[occurrence].push(userId);
  return acc;
}, {});

console.log(newDict);
