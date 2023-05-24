#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, function (err, res, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(data).title);
  }
});
