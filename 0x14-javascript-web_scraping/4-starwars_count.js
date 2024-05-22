#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  let counter = 0;

  data.results.forEach(result => {
    result.characters.forEach(character => {
      if (character.includes('/18/')) {
        counter++;
      }
    });
  });
  console.log(counter);
});
