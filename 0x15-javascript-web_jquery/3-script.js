// adds the class red to the <header> element when the
// user clicks on the tag DIV#red_header
const $ =  window.$;
$('DIV#red_header').click(function () {
    $('HEADER').addClass('red');
});
