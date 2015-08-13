$(document).ready(function(){
    window.setInterval(get_requests, 1000);
});


var get_requests = function(){
    $.ajax({
        url:'request/ajax/getrequests/',
        type:'GET',
        dataType: 'json',
        success: show_requests,
        error:function(data){console.error(data)}
    });
};


var show_requests = function(requests){
    var table_data='';

    for (var i in requests){
        var request = requests[i];
        table_data += '<tr><td>'+request.fields.uri+'</td><td>'+request.fields.time+'</td></tr>';
    }

    var table=$('table#example');
    var thead = '<<thead><tr><th>URI</th><th>TIME</th></tr></thead>';
    var tbody = '<tbody>'+table_data+'</tbody>';

    table.html(thead+tbody);
};