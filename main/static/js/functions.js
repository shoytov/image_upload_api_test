 $(document).ready(function(){
     $('#images_upload_form').on('submit', function(e) {
        e.preventDefault();
        var formData = new FormData(this);
        var form = $('#images_upload_form');

        $.ajax({
            url: form.attr('action'),
            type: form.attr('method'),
            dataType: 'json',
            contentType: false,
            processData: false,
            data: formData,
            cache: false,

            success: function (data) {
                console.log(data);
            },
            error: function (data) {
                console.log(data);
            }
        });
        return false;
    });
 });