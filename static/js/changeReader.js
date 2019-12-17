$(function () {
    $('#rdName, #rdDept, #rdPhone, #rdEmail').characterCounter();
    $('select').formSelect();
    function isEmpty() {
        let rdID = $('#rdID').val();
        let rdName = $('#rdName').val();
        let rdSex = $('#rdSex').val();
        let rdType = $('#rdType').val();
        let rdDept = $('#rdDept').val();
        let rdPhone = $('#rdPhone').val();
        let rdEmail = $('#rdEmail').val();

        if (rdID && rdName && rdSex && rdType && rdDept && rdPhone && rdEmail){
            $('#reader_change').attr('disabled', false);
        } else {
            $('#reader_change').attr('disabled', true);
        }
    }
    $('#rdID, #rdName, #rdDept, #rdPhone, #rdEmail').bind('input propertychange', function () {
        isEmpty();
    });
    $('#rdSex, #rdType').change(function () {
        isEmpty();
    });
    $('#reader_change').click(function () {
        $.ajax({
            url: '/api/reader/change',
            type: 'POST',
            data: {
                rdID: $('#rdID').val(),
                rdName: $('#rdName').val(),
                rdSex: $('#rdSex').val(),
                rdType: $('#rdType').val(),
                rdDept: $('#rdDept').val(),
                rdPhone: $('#rdPhone').val(),
                rdEmail: $('#rdEmail').val(),
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