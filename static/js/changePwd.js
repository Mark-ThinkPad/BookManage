$(function () {
    // 初始化input的计数器
    $('input#old_pwd, input#new_pwd, input#new_pwd_v').characterCounter();
    $('input#old_pwd, input#new_pwd, input#new_pwd_v').bind('input propertychange', function (event) {
        let old_pwd = $('#old_pwd').val();
        let new_pwd = $('#old_pwd').val();
        let new_pwd_v = $('#new_pwd_v').val();
        if (old_pwd && new_pwd && new_pwd_v) {
            $('#changePwd').attr('disabled', false);
        } else {
            $('#changePwd').attr('disabled', true);
        }
    });
    $('#changePwd').click(function () {
        let old_pwd = $('#old_pwd').val();
        let new_pwd = $('#new_pwd').val();
        let new_pwd_v = $('#new_pwd_v').val();
        if (old_pwd !== Cookies.get('pwd')) {
            alert('旧密码输入错误');
            $('#old_pwd').val('');
            $('#changePwd').attr('disabled', true);
            return false
        }
        if (new_pwd !== new_pwd_v) {
            alert('新密码两次输入不一致');
            $('#new_pwd').val('');
            $('#new_pwd_v').val('');
            $('#changePwd').attr('disabled', true);
            return false
        }
        $.ajax({
            url: '/api/user/changePwd',
            type: 'POST',
            data: {
                uid: Cookies.get('uid'),
                old_pwd: old_pwd,
                new_pwd: new_pwd,
            },
            dataType: 'json',
            success: function (data) {
                if (data.status === 1) {
                    alert(data.message);
                    window.location.href = '/user/login';
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