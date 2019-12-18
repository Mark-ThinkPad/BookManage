$(function () {
    $('#bkID').bind('input propertychange', function () {
        let bkID = $('#bkID').val();
        if (bkID) {
            $('#continue_status').attr('disabled', false);
        } else {
            $('#continue_status').attr('disabled', true);
        }
    });
    $('#continue_status').click(function () {
        $.ajax({
            url: '/api/borrow/continue/status',
            type: 'POST',
            data: {
                bkID: $('#bkID').val(),
            },
            dataType: 'json',
            success: function (data) {
                if (data.status === 1) {
                    alert(data.message);
                    $('#borrow_continue').attr('disabled', false);
                } else if (data.status === 0) {
                    alert(data.message);
                    $('#borrow_continue').attr('disabled', true);
                }
            },
            error: function (jpXHR) {
                alert('Status Code: ' + jpXHR.status);
            },
        });
    });
});