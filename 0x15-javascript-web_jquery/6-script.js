// updates the text of the <header> element
// when the user clicks on DIV#update_header.
const $ = window.$;
$('DIV#update_header').click(function (){
    $('HEADER').text('New Header!!!');
});