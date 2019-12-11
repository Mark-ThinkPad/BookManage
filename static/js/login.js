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

    });
    // 点击注册按钮跳转至注册页面
    $('#register').click(function () {
        window.location.href = '/register';
    });
});