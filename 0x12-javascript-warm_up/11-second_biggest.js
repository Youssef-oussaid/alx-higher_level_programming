#!/usr/bin/node
const len = process.argv.length;
if (len < 3) {
  console.log(1);
} else {
  let max = Number(process.argv[2]);
  for (let i = 3; i < len; i++) {
    if (Number(process.argv[i]) > max) {
      max = Number(process.argv[i]);
    }
  }
  console.log(max);
}
