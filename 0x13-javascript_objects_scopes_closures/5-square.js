#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  print() {
    for (let i = 0; i < this.size; i++) {
      console.log('X'.repeat(this.size));
    }
  }

  double() {
    this.size *= 2;
  }
}
module.exports = Square;
