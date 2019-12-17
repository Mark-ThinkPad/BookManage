$(function () {
    $('#bkID_f').bind('input propertychange', function () {
        let bkID = $('#bkID_f').val();
        if (bkID) {
            $('#book_find').attr('disabled', false);
        } else {
            $('#book_find').attr('disabled', true);
        }
    });
    $('#book_find').click(function () {
        $.ajax({
            url: '/api/book/find',
            type: 'POST',
            data: {
                bkID: $('#bkID_f').val(),
            },
            dataType: 'json',
            success: function (data) {
                if (data.status === 1) {
                    alert(data.message);
                    $('#bkID_f').val(data.bkID);
                    $('#bkName_f').val(data.bkName);
                    $('#bkAuthor_f').val(data.bkAuthor);
                    $('#bkPress_f').val(data.bkPress);
                    M.updateTextFields();
                    $('#toChange').attr('disabled', false);
                } else if (data.status === 0) {
                    alert(data.message);
                }
            },
            error: function (jpXHR) {
                alert('Status Code: ' + jpXHR.status);
            },
        });
    });
    $('#toChange').click(function () {
        $('#bkID_c').val($('#bkID_f').val());
        $('#bkName_c').val($('#bkName_f').val());
        $('#bkAuthor_c').val($('#bkAuthor_f').val());
        $('#bkPress_c').val($('#bkPress_f').val());
        M.updateTextFields();
    });
});