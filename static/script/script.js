$(document).ready(function () {
    actions();
});

function actions() {
    $("#send_button").on('click', send_form_data);

}

function send_form_data() {
    // var formData = new FormData();
    // formData.append("userfile", fileInputElement.files[0]);


    var form = document.querySelector("#data_form");
    var data = new FormData(form);


    // data = $("#data_form").serialize();
    console.log(data);
    $.ajax({
        url: '/save_form',
        type: "POST",
        data: data,
        processData: false,
        success: function () {

            alert('Load was performed.');
        }
    });


}