// fetches and shows the translation of hello.
const $ = window.$;
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
});