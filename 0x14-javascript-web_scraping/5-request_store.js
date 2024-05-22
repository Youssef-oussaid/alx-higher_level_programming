#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }

  const contentType = response.headers['content-type'];

  if (contentType && contentType.includes('application/json')) {
    const data = JSON.parse(body);
    fs.writeFile(filePath, JSON.stringify(data, null, 2), 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
