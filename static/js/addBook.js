$(function () {
    $('#bkName, #bkAuthor, #bkPress').characterCounter();
    $('#bkName, #bkAuthor, #bkPress, #bkNum').bind('input propertychange', function () {
        let bkName = $('#bkName').val();
        let bkAuthor = $('#bkAuthor').val();
        let bkPress = $('#bkPress').val();
        let bkNum = $('#bkNum').val();
        if (bkName && bkAuthor && bkPress && bkNum) {
            $('#book_add').attr('disabled', false);
        } else {
            $('#book_add').attr('disabled', true);
        }
    });
    $('#book_add').click(function () {
        $.ajax({
            url: '/api/book/add',
            type: 'POST',
            data: {
                bkName: $('#bkName').val(),
                bkAuthor: $('#bkAuthor').val(),
                bkPress: $('#bkPress').val(),
                bkNum: $('#bkNum').val(),
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