$(document).ready(function () {
    actions();
});

function actions() {
    $("#send_button").on('click', send_form_data);

}

function send_form_data() {
    form = $( "#data_form" )[0];
    var data = new FormData(form);
    $.ajax({
        url: '/save_form',
        type: "POST",
        data: data,
        processData: false,
        success: function () {
            alert('++++');
        }
    });


}