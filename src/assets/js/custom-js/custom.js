$(function() {
  var effects = 'animated bounce';
  var effectsEnd = 'animationend onAnimationEnd mozAnimationEnd webkitAnimationEnd';

  $('button.notify').hover(function() {
    $(this).addClass(effects).one(effectsEnd, function() {
      $(this).removeClass(effects);
    });
  });
});



$(document).ready(function() {
  $('.popup').click(function() {
    var src = $(this).attr('src'); 
    $('.modal').modal('show');
    $('#popup-img').attr('src', src)  
  });
});

