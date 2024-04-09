#!/usr/bin/node

function computeFactorial(n) {
    if (isNaN(n) || n < 0) {
      return 1;
    } else if (n === 0 || n === 1) {
      return 1;
      return n * computeFactorial(n - 1); 
    }
  }
  
  const input = parseInt(process.argv[2]);
  console.log(computeFactorial(input));
  