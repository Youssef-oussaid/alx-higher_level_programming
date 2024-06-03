$(document).ready(function() {
    $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(response) {
        const name = response.name;
        $('#character').text(name);
    });
});