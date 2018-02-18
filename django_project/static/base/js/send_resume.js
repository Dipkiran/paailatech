/**
 * Created by alan_shrestha on 6/21/17.
 */


function sendMessage(){
    var frm = $('#resumeForm');
    console.log(frm.serialize());
    var formData = new FormData($('#resumeForm')[0]);
    $.ajax({
        type: frm.attr('method'),
        url: frm.attr('action'),
        data: formData,

        success: function(response){
            //alert("Your message has been sent successfully");
            $("#resumeForm").html(response);
        },
        error: function(data){
            $("#resumeformMessage").html('There was an error sending your message');
        }
    });
}


$('#resumeForm').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted");
    $("#resumeformMessage").html("Sending Application. Please Wait...");
    var frm = $('#resumeForm');
    var formData = new FormData($(this)[0]);
    $.ajax({
        type: frm.attr('method'),
        url: frm.attr('action'),
        data: formData,
        processData: false,
        contentType: false,
        cache: false,
        async: false,

        success: function(response){
            //alert("Your message has been sent successfully");
            $("#resumeForm").html(response);
        },
        error: function(data){
            $("#resumeformMessage").html('There was an error sending your application');
        }
    });
})
/**
 * Created by alan_shrestha on 6/23/17.
 */
