$(function () {
    $('#bkID_s').bind('input propertychange', function () {
        let bkID = $('#bkID_s').val();
        if (bkID) {
            $('#book_status').attr('disabled', false);
        } else {
            $('#book_status').attr('disabled', true);
        }
    });
    $('#book_status').click(function () {
        $.ajax({
            url: '/api/borrow/add/status/book',
            type: 'POST',
            data: {
                bkID: $('#bkID_s').val(),
            },
            dataType: 'json',
            success: function (data) {
                if (data.status === 1) {
                    alert(data.message);
                } else if (data.status === 0) {
                    alert(data.message);
                    $('#borrow_add').attr('disabled', true);
                }
            },
            error: function (jpXHR) {
                alert('Status Code: ' + jpXHR.status);
            },
        });
    });
});