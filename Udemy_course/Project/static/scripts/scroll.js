$(document).ready(function() {
    $('#menu').on('click', 'a', function (e) {
        e.preventDefault();
        let id = $(this).attr('href'),
            top = $(id).offset().top;
        $('body, html').animate({scrollTop: top}, 500);
    });
});
