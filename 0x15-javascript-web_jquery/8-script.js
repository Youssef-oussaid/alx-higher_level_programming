$(document).ready(function() {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(response) {
        const films = response.results;
        const list_titles = $('#list_movies');

        films.forEach(film => {
            list_titles.append('<li>' + film.title + '<li>');
        });
    });
});