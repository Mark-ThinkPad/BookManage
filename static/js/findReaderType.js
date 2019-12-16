$(function () {
    $('#rdType_f, #rdTypeName_f').characterCounter();
    $('#rdType_f, #rdTypeName_f').bind('input propertychange', function () {
        let rdType = $('#rdType_f').val();
        let rdTypeName = $('#rdTypeName_f').val();
        if (rdType || rdTypeName) {
            $('#findReaderType').attr('disabled', false);
        } else {
            $('#findReaderType').attr('disabled', true);
        }
    });
    $('#findReaderType').click(function () {
        let rdType = $('#rdType_f').val();
        let rdTypeName = $('#rdTypeName_f').val();
        let data = {};
        if (rdType !== '') {
            data.rdType = rdType;
        }
        if (rdTypeName !== '') {
            data.rdTypeName = rdTypeName;
        }
        $.ajax({
            url: '/api/reader/type/find',
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (data) {
                if (data.status === 1) {
                    alert(data.message);
                    $('#rdType_f').val(data.rdType);
                    $('#rdTypeName_f').val(data.rdTypeName);
                    $('#CanLendQty_f').val(data.CanLendQty);
                    $('#CanLendDay_f').val(data.CanLendDay);
                    $('#CanContinueTimes_f').val(data.CanContinueTimes);
                    $('#PunishRate_f').val(data.PunishRate);
                    $('#DateValid_f').val(data.DateValid);
                    M.updateTextFields();
                    $('#migrateData').attr('disabled', false);
                } else if (data.status === 0) {
                    alert(data.message);
                }
            },
            error: function (jpXHR) {
                alert('Status Code: ' + jpXHR.status);
            },
        });
    });
    $('#migrateData').click(function () {
        $('#rdType_c').val($('#rdType_f').val());
        $('#rdTypeName_c').val($('#rdTypeName_f').val());
        $('#CanLendQty_c').val($('#CanLendQty_f').val());
        $('#CanLendDay_c').val($('#CanLendDay_f').val());
        $('#CanContinueTimes_c').val($('#CanContinueTimes_f').val());
        $('#PunishRate_c').val($('#PunishRate_f').val());
        $('#DateValid_c').val($('#DateValid_f').val());
        M.updateTextFields();
    });
});