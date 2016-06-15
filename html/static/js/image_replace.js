$('.picture').click(function(){ 
  var src = $(this).attr('src');
  var tmp = $(this).data('alt-image');
  $(this).attr('src', tmp);
  $(this).data('alt-image', src);
});
