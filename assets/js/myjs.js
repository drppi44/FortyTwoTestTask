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


function force_is_viewed(){
    $.get('/ajax/request/update/')
        .done(get_requests)
}


var show_requests = function(data){
    $('#request_table').html(data.text);
    $('title').html('('+data.count+') 42 Coffee Cups Test Assignment');
    $('.container h1').html('('+data.count+') 42 Coffee Cups Test Assignment. Middleware.')
};
var refresh_is_viewed_time = 5;

$(document).ready(function(){
    window.setInterval(function(){
        // update page
        if (refresh_is_viewed_time === 0){
            force_is_viewed();
            refresh_is_viewed_time = 6;
        }
        // decrease timer
        if (document.visibilityState === 'visible')
            refresh_is_viewed_time -= 1;
        else
            refresh_is_viewed_time = 6;

        // show timer
        $('span#timer').html(refresh_is_viewed_time)
    },1000)
});

