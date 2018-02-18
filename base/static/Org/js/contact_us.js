/**
 * Created by alan_shrestha on 6/21/17.
 */


function sendMessage(){
    var frm = $('#contactForm');
    console.log(frm.serialize());
    $.ajax({
        type: frm.attr('method'),
        url: frm.attr('action'),
        data: frm.serialize(),
        success: function(response){
            //alert("Your message has been sent successfully");
            $("#contactForm").html(response);
        },
        error: function(data){
            $("#contactformMessage").html('There was an error sending your message');
        }
    });
}


$('#contactForm').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted");
    $("#contactformMessage").html("Sending Inquiry...");
    sendMessage();
})
