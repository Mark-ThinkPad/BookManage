$(function () {
    $('#rdID_s').bind('input propertychange', function () {
        let rdID = $('#rdID_s').val();
        if (rdID) {
            $('#reader_status').attr('disabled', false);
        } else {
            $('#reader_status').attr('disabled', true);
        }
    });
    $('#reader_status').click(function () {
        $.ajax({
            url: '/api/borrow/add/status/reader',
            type: 'POST',
            data: {
                rdID: $('#rdID_s').val(),
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