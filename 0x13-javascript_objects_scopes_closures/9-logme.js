#!/usr/bin/node
let logMeCounter = 0;

exports.logMe = function (item) {
  console.log(logMeCounter + ': ' + item);
  logMeCounter++;
};
