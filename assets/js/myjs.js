$(document).ready(function(){
    get_requests();
});





var get_requests = function(){
    $.ajax({
        url:'/ajax/getrequests/',
        type:'GET',
        dataType: 'json',
        success: show_requests,
        error:function(data){console.error(data)}
    });
};


var show_requests = function(requests){
    console.log(requests);
    var table_data='';
    for (var i in requests){
        var request = requests[i];
        table_data += '<tr><td>'+request.fields.uri+'</td><td>'+request.fields.time+'</td></tr>';
    }
    $('#request_table').html(table_data);
};