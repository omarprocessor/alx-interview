#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const characters = JSON.parse(body).characters;

  characters.forEach((url) => {
    request(url, (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
