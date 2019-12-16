$(function () {
    // 初始化input的计数器
    $('#rdType_c, #rdTypeName_c, #DateValid_c').characterCounter();
    // 前端判断输入是否为空, 为空时禁用按钮
    $('#rdType_c, #rdTypeName_c, #CanLendQty_c, #CanLendDay_c, #CanContinueTimes_c, #PunishRate_c, #DateValid_c').bind('input propertychange', function (event) {
        let rdType = $('#rdType_c').val();
        let rdTypeName = $('#rdTypeName_c').val();
        let CanLendQty = $('#CanLendQty_c').val();
        let CanLendDay = $('#CanLendDay_c').val();
        let CanContinueTimes = $('#CanContinueTimes_c').val();
        let PunishRate = $('#PunishRate_c').val();
        let DateValid = $('#DateValid_c').val();
        if (rdType && rdTypeName && CanLendQty && CanLendDay && CanContinueTimes && PunishRate && DateValid) {
            $('#changeReaderType').attr('disabled', false);
        } else {
            $('#changeReaderType').attr('disabled', true);
        }
    });
    $('#changeReaderType').click(function () {
        $.ajax({
            url: '/api/reader/type/change',
            type: 'POST',
            data: {
                rdType: $('#rdType_c').val(),
                rdTypeName: $('#rdTypeName_c').val(),
                CanLendQty: $('#CanLendQty_c').val(),
                CanLendDay: $('#CanLendDay_c').val(),
                CanContinueTimes: $('#CanContinueTimes_c').val(),
                PunishRate: $('#PunishRate_c').val(),
                DateValid: $('#DateValid_c').val(),
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