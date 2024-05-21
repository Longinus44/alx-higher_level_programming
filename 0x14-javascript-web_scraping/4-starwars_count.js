#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

if (!apiUrl) {
  console.error('Please provide the API URL as the first argument.');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  try {
    const films = JSON.parse(body).results;
    const moviesWithWedgeAntilles = films.filter(film =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
    console.log(`${moviesWithWedgeAntilles.length}`);
  } catch (error) {
    console.error(error);
  }
});
