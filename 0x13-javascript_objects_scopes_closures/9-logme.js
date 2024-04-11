#!/usr/bin/node
let logMeCounter = 0;

exports.logMe = function (item) {
  console.log(logMe + ': ' + item);
  logMeCounter++;
};
