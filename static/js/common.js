$(document).ready(function () {
    $('.sidenav').sidenav();
    let uid = Cookies.get('uid');
    let pwd = Cookies.get('pwd');
    let username = Cookies.get('username');
    if (uid && pwd && username) {
        $('#user').html('<a class="dropdown-trigger" data-target="dropdown"><i class="material-icons left">person_pin</i>'
            + username + '<i class="material-icons right">arrow_drop_down</i></a>');
        $('.dropdown-trigger').dropdown();
        $('#user_m').html('<a class="waves-effect waves-light"><i class="material-icons left">person_pin</i>'
            + username + '</a>');
        $('ul#mobile-sidenav').append('<li><a class="waves-effect waves-light" href="/user/changePwd"><i class="material-icons">vpn_key</i>修改密码</a></li>\n'
            + '<li><a class="waves-effect waves-light" id="logout_m"><i class="material-icons">exit_to_app</i>退出登录</a></li>');
    }
    $('#logout, #logout_m').click(function () {
        Cookies.remove('uid');
        Cookies.remove('pwd');
        Cookies.remove('username');
        window.location.reload();
    });
});