$(function() {
  var effects = 'animated bounce';
  var effectsEnd = 'animationend onAnimationEnd mozAnimationEnd webkitAnimationEnd';

  $('a.button').hover(function() {
    $(this).addClass(effects).one(effectsEnd, function() {
      $(this).removeClass(effects);
    });
  });
});