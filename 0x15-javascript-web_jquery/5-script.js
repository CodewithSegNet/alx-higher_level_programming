const $ = window.$;

$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });
});
