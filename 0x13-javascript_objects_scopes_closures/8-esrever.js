#!/usr/bin/node
exports.esrever = function (list) {
  let esrever = [];
  for (let i = (list.length - 1); i >=0; i--) {
    esrever.append(list[i]);
  }
  return esrever;
};