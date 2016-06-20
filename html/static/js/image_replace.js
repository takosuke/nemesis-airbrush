$(function() {

  $('.picture').click(function(){ 

    var active = $('.active-img').first();
    if(active){
      console.log(active.attr('src'));
      var src = active.attr('src');
      var tmp = active.data('alt-image');
      active.attr('src', tmp);
      active.data('alt-image', src);
      active.removeClass('active-img');
    }

    selected = $(this);
    src = selected.attr('src');
    tmp = selected.data('alt-image');
    selected.attr('src', tmp);
    selected.data('alt-image', src);
    selected.addClass('active-img');
  });

});
