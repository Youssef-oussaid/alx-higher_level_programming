#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; Number(argv[2]) > i; i++) {
    console.log('C is fun');
  }
}
