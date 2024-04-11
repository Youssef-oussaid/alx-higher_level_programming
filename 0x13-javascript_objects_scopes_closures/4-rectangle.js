#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      let i = 0;
      while (this.height > i) {
        let j = 0;
        let row = '';
        while (this.width > j) {
          row += 'X';
          j++;
        }
        console.log(row);
        i++;
      }
    }

    rotate () {
      this.height = this.width;
      this.width = this.height;
    }

    double () {
      this.height * 2;
      this.width * 2;
    }
  }
  module.exports = Rectangle;
  