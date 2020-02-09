$(document).ready(function () {
    $('#id_form').submit(function (e) {
        e.preventDefault();
        $form = $(this);
        var formData = new FormData(this);
        $.ajax({
            url: "/registration",
            type: 'POST',
            data: formData,
            success: function (response) {
                alert(response);
                window.location.href = '/';
            },
            cache: false,
            contentType: false,
            processData: false
        });
    });


    $('#id_login_form').submit(function (e) {
        e.preventDefault();
        $form = $(this);
        var formData = new FormData(this);
        $.ajax({
            url: "/user_login",
            type: 'POST',
            data: formData,
            success: function (response) {
                location.reload();
            },
            cache: false,
            contentType: false,
            processData: false
        });
    });

    $('#id_profile_form').submit(function (e) {
        e.preventDefault();
        $form = $(this);
        var formData = new FormData(this);
        $.ajax({
            url: "/updata_user_info",
            type: 'POST',
            data: formData,
            success: function () {
                location.reload();
            },
            cache: false,
            contentType: false,
            processData: false
        });
    });



    $('#comment_form_2').submit(function (e) {
        e.preventDefault();
        $form = $(this);
        var formData = new FormData(this);
        id = $("#a_job_id").val();
        formData.append("job_id", id);
        $.ajax({
            url: "/add_comment",
            type: 'POST',
            data: formData,
            success: function (response) {
                location.reload();
            },
            cache: false,
            contentType: false,
            processData: false
        });
    });
});


// $('#id_ajax_upload_form').submit(function(e){
//        e.preventDefault();
//        $form = $(this);
//        var formData = new FormData(this);
//        $.ajax({
//            url: "/save_form",
//            type: 'POST',
//            data: formData,
//            success: function (response) {
//                alert("+++")
//            }
//            ,
//            cache: false,
//            contentType: false,
//            processData: false
//        });
//    });

// function actions() {
//     $("#send_button").on('click', send_form_data);
// }

// function send_form_data() {
//     // var formData = new FormData();
//     // formData.append("userfile", fileInputElement.files[0]);
//     var form = document.querySelector("#data_form");
//     var data = new FormData(form);


// // data = $("#data_form").serialize();
// console.log(data);
// $.ajax({
//     url: '/save_form',
//     type: "POST",
//     data: data,
//     processData: false,
//     success: function () {
//
//         alert('Load was performed.');
//     }
//     });
//
//
// }