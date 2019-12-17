$(function () {
    $('#rdID').bind('input propertychange', function () {
        let rdID = $('#rdID').val();
        if (rdID) {
            $('#reader_loss_report').attr('disabled', false);
        } else {
            $('#reader_loss_report').attr('disabled', true);
        }
    });
    $('#reader_loss_report').click(function () {
        $.ajax({
            url: '/api/reader/loss/report',
            type: 'POST',
            data: {
                rdID: $('#rdID').val(),
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