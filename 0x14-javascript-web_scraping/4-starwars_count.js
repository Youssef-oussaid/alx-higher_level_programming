#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/18';
request(url, (error,response, body) => {
    if (error){
        console.error(error);
        return;
    }
    const data = JSON.parse(body)
    let counter = data.films.length;
    console.log(counter);
});