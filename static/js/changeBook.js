$(function () {
    $('#bkName_c, #bkAuthor_c, #bkPress_c').characterCounter();
    $('#bkName_c, #bkAuthor_c, #bkPress_c, #bkID_c').bind('input propertychange', function () {
        let bkID = $('#bkID_c').val();
        let bkName = $('#bkName_c').val();
        let bkAuthor = $('#bkAuthor_c').val();
        let bkPress = $('#bkPress_c').val();
        if (bkName && bkAuthor && bkPress && bkID) {
            $('#book_change').attr('disabled', false);
        } else {
            $('#book_change').attr('disabled', true);
        }
    });
    $('#book_change').click(function () {
        $.ajax({
            url: '/api/book/change',
            type: 'POST',
            data: {
                bkID: $('#bkID_c').val(),
                bkName: $('#bkName_c').val(),
                bkAuthor: $('#bkAuthor_c').val(),
                bkPress: $('#bkPress_c').val(),
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