$(document).ready(function() {
    var options = {
        beforeSubmit:  preSubmit,
        success:       showResponse,
        error:         showResponse,

        dataType:  'json'
    }; 
 
    // bind to the form's submit event 
    $('#edit-form').submit(function() {
        $(this).ajaxSubmit(options); 

        return false
    });
}); 
 
// pre-submit callback 
function preSubmit(formData, jqForm, options) {

    $('[type=submit]').button('loading');
    $('form :input').attr('disabled', true);
    return true;
} 
 
// post-submit callback 
function showResponse(responseText, statusText, xhr, $form)  {
    console.log(responseText);
    setTimeout(function () {
        $('[type=submit]').button('reset');
        $('form :input').attr('disabled', false);
    }, 1000);
}

// avatar preview ===================================
function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('img#preview').attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}
$(document).on('change', '#id_avatar', function(){
    readURL(this);
    console.log('dasda');
});
//===================================================