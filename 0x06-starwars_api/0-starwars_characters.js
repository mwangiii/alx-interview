#!/usr/bin/node

const request = require('request')

// The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi” 
const movieId = process.argv[2]

if (!movieId) {
  console.error('Please provide a movie ID as a command line argument.');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Unexpected status code: ${response.statusCode}`);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie.');
    process.exit(0);
  }

  // Displaying one character name per line
  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (!charError && charResponse.statusCode === 200) {
        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      } else {
        console.error('Error fetching character:', charError);
      }
    });
  });
});
