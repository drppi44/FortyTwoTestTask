$(document).ready(function(){
    get_requests();
    window.setInterval(get_requests, 1000);
});


function get_requests(){
    $.ajax({
        url:'request/ajax/getrequests/',
        type:'GET',
        dataType: 'json',
        success: show_requests,
        error:function(data){console.error(data)}
    });
}


var show_requests = function(data){
    var table=$('table#example tbody').html(data.text);
    $('title').html('('+data.count+') 42 Coffee Cups Test Assignment');
    $('.container h1').html('('+data.count+') 42 Coffee Cups Test Assignment. Middleware.')
};