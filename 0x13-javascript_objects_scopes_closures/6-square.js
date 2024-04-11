#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; this.height > i; i++) {
      let row = '';
      for (let j = 0; this.width > j; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
