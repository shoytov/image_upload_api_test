// refresh imageset
function imageset(){
    $.ajax({
        url: '/api-v1.0/images',
        dataType: 'json',
        contentType: false,
        processData: false,
        data: '',
        cache: false,

        success: function (data) {
            $('#imageset').html();

            html = '';
            for(i=0; i<data.length; i++){
                html += '<span><a href="' + data[i].img + '"><img src="'+ data[i].thumbnail +'"></a></span>'
                html += '<a href="javascript:delete_image('+ data[i].id +')">X</a>'
            }
            $('#imageset').html(html);
        },
        error: function (data) {
            console.log(data);
        }
    });
}


// delete picture by id
function delete_image(picture_id){
    $.ajax({
        url: '/api-v1.0/image/' + picture_id,
        dataType: 'json',
        type: 'delete',
        contentType: false,
        processData: false,
        data: '',
        cache: false,

        success: function (data) {
            imageset();
        },
        error: function (data) {
            console.log(data);
        }
    });
}

$(document).ready(function(){
    // form ajax upload
     $('#images_upload_form').on('submit', function(e) {
        var progressBar = $('#progressbar');
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

            xhr: function(){
                    var xhr = $.ajaxSettings.xhr(); // получаем объект XMLHttpRequest
                    xhr.upload.addEventListener('progress', function(evt){ // добавляем обработчик события progress (onprogress)
                      if(evt.lengthComputable) { // если известно количество байт
                        // высчитываем процент загруженного
                        var percentComplete = Math.ceil(evt.loaded / evt.total * 100);
                        // устанавливаем значение в атрибут value тега <progress>
                        // и это же значение альтернативным текстом для браузеров, не поддерживающих <progress>
                        progressBar.val(percentComplete).text('Загружено ' + percentComplete + '%');
                      }
                    }, false);
                    return xhr;
                  },

            success: function (data) {
                $("#id_image").val('');
                imageset();
                progressBar.val('');
            },
            error: function (data) {
                console.log(data);
            }
        });
        return false;
    });
 });