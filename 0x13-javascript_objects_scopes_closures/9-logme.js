#!/usr/bin/node
let logMe = 0;
exports.logMe = function (item) {
  console.log(logMe + ': ' + item)
  logMe += 1;
}
