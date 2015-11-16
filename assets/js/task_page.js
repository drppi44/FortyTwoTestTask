function getCookie(name)
{
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?

            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});

$(document).ready(
    function(){
        $("#sortable").sortable({
            update: function() {
                var task_pos = [];
                $("#sortable").children().each(function(i) {
                    task_pos.push({
                        key: $(this).attr("task_id"),
                        value: i
                    });
                });

                $.ajax({
                    type: "POST",
                    url: "/task/sort/",
                    data: JSON.stringify(task_pos),
                    dataType: 'json'

                }).fail(function(data){console.log(data)})
            }
        });
    }
);
