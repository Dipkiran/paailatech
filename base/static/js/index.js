$(document).ready(function(){$(".feature").mouseenter(function(){$(this).addClass("change");});$(".feature").mouseleave(function(){$(this).removeClass("change");});$(".products").mouseenter(function(){$(this).find("p").show();$(this).find("h2").show();});$(".products").mouseleave(function(){$(this).find("p").hide();$(this).find("h2").hide();});});