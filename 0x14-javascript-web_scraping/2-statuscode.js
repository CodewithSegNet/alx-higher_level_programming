#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, res, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(`code is ${res.statusCode}`);
  }
});
