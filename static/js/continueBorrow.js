$(function () {
    $('#borrow_continue').click(function () {
        $.ajax({
            url: '/api/borrow/continue',
            type: 'POST',
            data: {
                bkID: $('#bkID').val(),
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