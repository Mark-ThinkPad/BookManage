$(function () {
    $('#rdID_f').bind('input propertychange', function () {
        let rdID = $('#rdID_f').val();
        if (rdID) {
            $('#reader_loss_status').attr('disabled', false);
        } else {
            $('#reader_loss_status').attr('disabled', true);
        }
    });
    $('#reader_loss_status').click(function () {
        $.ajax({
            url: '/api/reader/loss/cancel/status',
            type: 'POST',
            data: {
                rdID: $('#rdID_f').val(),
            },
            dataType: 'json',
            success: function (data) {
                if (data.status === 1) {
                    alert(data.message);
                    $('#rdID').val($('#rdID_f').val());
                    M.updateTextFields();
                    $('#reader_loss_cancel').attr('disabled', false);
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