/*
updates the text color of the <header> element to red
(#FF0000) when the user clicks on the tag DIV#red_header
*/
const $ = window.$;
$('DIV#red_header').click(function () {
    $('HEADER').css('color', '#FF0000');
});