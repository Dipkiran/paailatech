$(document).ready(function(){

  // Carets
  $(".footer-col").find(".fa-angle-down").hide();
  $(".footer-col").find(".fa-angle-up").hide();
  $(".footer-col").find(".fa-angle-up").toggle();

  if ($(window).width() < 736) {
    /*Carets*/
    $(".footer-col").find(".fa-angle-down").hide();
    $(".footer-col").find(".fa-angle-up").hide();
    $(".footer-col").find(".fa-angle-down").toggle();

    $(".footer-col").removeClass("col-lg-2");
    $(".footer-col").removeClass("col-md-2");
    $(".footer-col").removeClass("col-sm-3");
    $(".footer-col").removeClass("col-xs-6");

    $(".footer-col").find("ul").hide();
  }

  else{
    // Add classes back
    $(".footer-col").find(".fa-angle-down").hide();
    $(".footer-col").find(".fa-angle-up").hide();
  }

  $(".footer-col").click(function(){
    if ($(window).width() < 736) {
      $(this).find("ul").slideToggle();
      $(this).find(".fa-angle-up").toggle();
      $(this).find(".fa-angle-down").toggle();
    }
  });

  $(window).resize(function(){
    var $width = $(window).width();
    $(".check").text("Screen width : " + $width);

    if ($(window).width() < 736) {
      /*Carets*/
      $(".footer-col").find(".fa-angle-down").hide();
      $(".footer-col").find(".fa-angle-up").hide();
      $(".footer-col").find(".fa-angle-down").toggle();

      $(".footer-col").removeClass("col-lg-2");
      $(".footer-col").removeClass("col-md-2");
      $(".footer-col").removeClass("col-sm-3");
      $(".footer-col").removeClass("col-xs-6");

      $(".footer-col").find("ul").hide();
  }

  else {
    $(".footer-col").find("ul").show();

    // Hide carets
    $(".footer-col").find(".fa-angle-down").hide();
    $(".footer-col").find(".fa-angle-up").hide();

    // Add classes back
    $(".footer-col").addClass("col-lg-2");
    $(".footer-col").addClass("col-md-2");
    $(".footer-col").addClass("col-sm-3");
    $(".footer-col").addClass("col-xs-6");

  }
});

});
