$(document).ready(function(){

  $(".feature").mouseenter(function(){
    // $(this).find("h1").css("display","none");
    $(this).addClass("change");
  });

  $(".feature").mouseleave(function(){
    // $(this).find("h1").css("display","none");
    $(this).removeClass("change");
  });

  $(".products").mouseenter(function(){
    $(this).find("p").show();
    $(this).find("h2").show();
  });

  $(".products").mouseleave(function(){
    $(this).find("p").hide();
    $(this).find("h2").hide();
  });



});
