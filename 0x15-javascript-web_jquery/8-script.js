// fetches and lists the title for all movies of Starwars.
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const content = data.results;
    for (let item = 0; item < content.length; item++) {
        $('UL#list_movies').append('<li>' + content[item].title + '</li>');   
    }
});