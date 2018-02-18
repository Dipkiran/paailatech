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

  $(".testimonial").click(function(){
    $(".testimonial").toggle();
    $(this).toggle();
    $(this).find(".image-testimonial").toggle();
  });


  $(".award").click(function(){
    $hello = $(this).find("h1").text();

    $h1 = $(this).find("h1").text();
    $message = $(this).find("#message").text();
    $quoteby = $(this).find("#quoteby").text();
    $caption = $(this).find("#caption").text();
    $image = $(this).find("img").attr("src");

    $(".award").show();
    $(this).toggle();

    $(".blank").find("h1").html($h1);
    $(".blank").find("#message").html($message);
    $(".blank").find("#quoteby").html($quoteby);
    $(".blank").find("#caption").html($caption);
    $(".blank").find("img").attr("src",$image);

    $("p").animate({left: '250px'});

  });
});
