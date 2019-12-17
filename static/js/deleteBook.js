$(function () {
    $('#bkID_d').bind('input propertychange', function () {
        let bkID = $('#bkID_d').val();
        if (bkID) {
            $('#book_delete').attr('disabled', false);
        } else {
            $('#book_delete').attr('disabled', true);
        }
    });
    $('#book_delete').click(function () {
        $.ajax({
            url: '/api/book/delete',
            type: 'POST',
            data: {
                bkID: $('#bkID_d').val(),
            },
            dataType: 'json',
            success: function (data) {
                if (data.status === 1) {
                    alert(data.message);
                } else if (data.status === 0) {
                    alert(data.message);
                }
            },
            error: function (jpXHR) {
                alert('Status Code: ' + jpXHR.status);
            },
        });
    });
});