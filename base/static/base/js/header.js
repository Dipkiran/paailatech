$(document).ready(function(){

  // Navigation icon-bar
  // $(".icon-bar").css("background","black");

  // On loading
  if ($(window).width() > 1000) {
    $(".navbar-header").removeClass("small");
    $(".navbar-header").addClass("large");
  }
  else {
  }

// large and small navbar on scrolling
    $(window).on("scroll", function(){
      if ($(window).width() > 800) {

        if($(window).scrollTop()>1){
          $(".navbar-header").addClass("small");
          $(".navbar-header").removeClass("large");

          // logo
          $(".logoblack").css("display","block");
          $(".logowhite").css("display","none");

        }
        else{
          $(".navbar-header").removeClass("small");
          $(".navbar-header").addClass("large");

          // logo
          $(".logowhite").css("display","block");
          $(".logoblack").css("display","none");
        }
      }
      else{
      }
  });
// End of navbar height change program

  // navbar overlay for fullscreen navigation bar
  $("#navbutton").click(function(){
    $(".navbar-header").toggleClass("navbar-overlay");
    $(".navbar-collapse").toggleClass("navbar-collapse-change");
    $("body").toggleClass("body-disable-scroll");
    $(".navbar-collapse").toggle();
  });


  // Reset navbar on resizing window
  $(window).resize(function(){
    if($(window).width()>660){
    $(".navbar-header").removeClass("navbar-overlay");
    $(".navbar-collapse").removeClass("navbar-collapse-change");
    $("body").removeClass("body-disable-scroll");
    $(".navbar-collapse").hide();
  }
  });


});
// End of document
