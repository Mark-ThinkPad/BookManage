$(function () {
    $('#rdID_f').bind('input propertychange', function () {
        let rdID = $('#rdID_f').val();
        if (rdID) {
            $('#reader_status').attr('disabled', false);
        } else {
            $('#reader_status').attr('disabled', true);
        }
    });
    $('#reader_status').click(function () {
        $.ajax({
            url: '/api/reader/add/status',
            type: 'POST',
            data: {
                rdID: $('#rdID_f').val(),
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