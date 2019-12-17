$(function () {
    $('#rdID, #bkID').bind('input propertychange', function () {
        let rdID = $('#rdID').val();
        let bkID = $('#bkID').val();
        if (rdID && bkID) {
            $('#borrow_add').attr('disabled', false);
        } else {
            $('#borrow_add').attr('disabled', true);
        }
    });
    $('#borrow_add').click(function () {
        $.ajax({
            url: '/api/borrow/add',
            type: 'POST',
            data: {
                rdID: $('#rdID').val(),
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