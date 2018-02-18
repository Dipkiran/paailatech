$(document).ready(function(){

  $("#faq").click(function(event){
    event.stopImmediatePropagation();
    $(".question-answer").slideToggle();
    $(this).find(".fa-angle-up").toggle();
    $(this).find(".fa-angle-down").toggle();
  });

  $(".question-answer").click(function(event){
    event.stopImmediatePropagation();
    $(this).find("p").slideToggle();
    $(this).find(".answer").slideToggle();
    $(this).find(".fa-plus").toggle();
    $(this).find(".fa-times").toggle();
  });

});
