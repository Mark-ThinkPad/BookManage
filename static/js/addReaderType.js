$(function () {
    // 初始化input的计数器
    $('#rdType, #rdTypeName, #DateValid').characterCounter();
    // 前端判断输入是否为空, 为空时禁用按钮
    $('#rdType, #rdTypeName, #CanLendQty, #CanLendDay, #CanContinueTimes, #PunishRate, #DateValid').bind('input propertychange', function (event) {
        let rdType = $('#rdType').val();
        let rdTypeName = $('#rdTypeName').val();
        let CanLendQty = $('#CanLendQty').val();
        let CanLendDay = $('#CanLendDay').val();
        let CanContinueTimes = $('#CanContinueTimes').val();
        let PunishRate = $('#PunishRate').val();
        let DateValid = $('#DateValid').val();
        if (rdType && rdTypeName && CanLendQty && CanLendDay && CanContinueTimes && PunishRate && DateValid) {
            $('#addReaderType').attr('disabled', false);
        } else {
            $('#addReaderType').attr('disabled', true);
        }
    });
    $('#addReaderType').click(function () {
        $.ajax({
            url: '/api/reader/type/add',
            type: 'POST',
            data: {
                rdType: $('#rdType').val(),
                rdTypeName: $('#rdTypeName').val(),
                CanLendQty: $('#CanLendQty').val(),
                CanLendDay: $('#CanLendDay').val(),
                CanContinueTimes: $('#CanContinueTimes').val(),
                PunishRate: $('#PunishRate').val(),
                DateValid: $('#DateValid').val(),
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