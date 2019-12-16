$(function () {
    $('#rdType_d, #rdTypeName_d').characterCounter();
    $('#rdType_d, #rdTypeName_d').bind('input propertychange', function () {
        let rdType = $('#rdType_d').val();
        let rdTypeName = $('#rdTypeName_d').val();
        if (rdType || rdTypeName) {
            $('#deleteReaderType').attr('disabled', false);
        } else {
            $('#deleteReaderType').attr('disabled', true);
        }
    });
    $('#deleteReaderType').click(function () {
        let rdType = $('#rdType_d').val();
        let rdTypeName = $('#rdTypeName_d').val();
        let data = {};
        if (rdType !== '') {
            data.rdType = rdType;
        }
        if (rdTypeName !== '') {
            data.rdTypeName = rdTypeName;
        }
        $.ajax({
            url: '/api/reader/type/delete',
            type: 'POST',
            data: data,
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