#!/usr/bin/node

const fs = require('fs');
const [,, fileA, fileB, fileC] = process.argv;

function concatFiles (source1, source2, destination) {
  fs.readFile(source1, 'utf8', (err, data1) => {
    if (err) throw err;
    fs.readFile(source2, 'utf8', (err, data2) => {
      if (err) throw err;
      fs.writeFile(destination, data1 + data2, (err) => {
        if (err) throw err;
      });
    });
  });
}

concatFiles(fileA, fileB, fileC);
