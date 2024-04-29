#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const size = Number(argv[2]);
  let i = 0;
  while (size > i) {
    let j = 0;
    let row = '';
    while (size > j) {
      row += 'X';
      j++;
    }
    console.log(row);
    i++;
  }
}
