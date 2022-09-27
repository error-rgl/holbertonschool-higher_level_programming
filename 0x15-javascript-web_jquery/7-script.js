// fetches and lists the character names for a movie of Starwars
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    $('DIV#character').text(data.name);
});