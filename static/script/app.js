$(document).on("keypress", ".code", function() {
    req = $.ajax({
        type: 'POST',
        url: '/submit',
        data: {
            code: $("#code").val()
        }
    });
    req.done(function(data) {
        $("#outputs").html(data);
        // console.log("helloj");

    });
});

function backspace(keycode) {
    if (keycode == 8) {

        req = $.ajax({
            type: 'POST',
            url: '/submit',
            data: {
                code: $("#code").val()

            }
        });
        req.done(function(data) {
            $("#outputs").html(data);

            // console.log("initialize");
        })
    }
};