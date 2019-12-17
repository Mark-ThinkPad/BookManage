$(function () {
    $('#rdID').bind('input propertychange', function () {
        let rdID = $('#rdID').val();
        if (rdID) {
            $('#reader_replace').attr('disabled', false);
        } else {
            $('#reader_replace').attr('disabled', true);
        }
    });
    $('#reader_replace').click(function () {
        $.ajax({
            url: '/api/reader/replace',
            type: 'POST',
            data: {
                rdID: $('#rdID').val(),
            },
            dataType: 'json',
            success: function (data) {
                if (data.status === 1) {
                    alert(data.message);
                    $('#main').append('<div class="center">\n' +
                        '        <h5 id="menu-nav">新的借书证号为: ' + data.new_rdID +  '</h5>\n' +
                        '    </div>');
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