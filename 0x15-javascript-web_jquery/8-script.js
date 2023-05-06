$(document).ready(function() {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
	var movies = data.results;
	$.each(movies, function(index, movie) {
	    $('ul#list_movies').append($('<li>').text(movie.title));
	});
    });
});
