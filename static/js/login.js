$(function () {
    // 初始化input的计数器
    $('input#pwd').characterCounter();
    // 前端判断输入是否为空, 为空时禁用按钮
    $('input#uid, input#pwd').bind('input propertychange', function (event) {
        let uid = $('#uid').val();
        let pwd = $('#pwd').val();
        if (uid && pwd) {
            $('#login').attr('disabled', false);
        } else {
            $('#login').attr('disabled', true);
        }
    });
    // 回车触发按钮点击事件
    $('#uid, #pwd').keydown(function (event) {
        if (event.keyCode === 13) {
            if ($('#login').prop('disabled') === true) {
                M.toast({html: '请输入完整的用户名和密码'});
            } else {
                $('#login').click();
            }
        }
    });
    // 点击登录按钮后向后端API发送数据
    $('#login').click(function () {
        $.ajax({
            url: '/api/user/login',
            type: 'POST',
            data: {
                uid: $('#uid').val(),
                pwd: $('#pwd').val(),
            },
            dataType: 'json',
            success: function (data) {
                if (data.status === 1) {
                    alert(data.message);
                    // 将登录信息添加到cookies
                    Cookies.set('uid', data.uid);
                    Cookies.set('pwd', data.pwd);
                    Cookies.set('username', data.username);
                    // 返回上一页并刷新
                    window.location.href=document.referrer||host + '';
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