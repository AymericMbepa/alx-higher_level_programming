$(document).ready(function() {
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
	var helloTranslation = data.hello;
	$('div#hello').text(helloTranslation);
    });
});
