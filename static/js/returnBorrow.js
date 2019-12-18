$(function () {
    $('#bkID, #rdID').bind('input propertychange', function () {
        let bkID = $('#bkID').val();
        let rdID = $('#rdID').val();
        if (bkID && rdID) {
            $('#borrow_return').attr('disabled', false);
        } else {
            $('#borrow_return').attr('disabled', true);
        }
    });
    $('#borrow_return').click(function () {
        $.ajax({
            url: '/api/borrow/return',
            type: 'POST',
            data: {
                bkID: $('#bkID').val(),
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