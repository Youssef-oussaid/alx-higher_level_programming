#!/usr/bin/node
let logMeCounter = 0;

exports.logMe = function (item) {
<<<<<<< HEAD
  console.log(logMe + ': ' + item);
  logMe += 1;
=======
  console.log(logMeCounter + ': ' + item);
  logMeCounter++;
>>>>>>> 298d27d1cccceec1b7df224e39ab30dd11502367
};
