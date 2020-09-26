window.onpageshow = function (event) {
    if (event.persisted || (window.performance && window.performance.navigation.type == 2)) {
        window.location.reload();
    }
}

$(function () {
    $('.mv_zone').sortable({
        revert: true,
        tolerance: "intersect",
        connectWith: ".mv_zone",
        handle: ".title",
        placeholder: "item-placeholder",
        update: function (event, ui) {
            if (this === ui.item.parent()[0]) {
                var pk = $(ui.item).data('no');
                var status = $(ui.item).closest('.area_zone').data('status');
                console.log(status);
                $.ajax({
                    type: "POST",
                    url: myGlobal.url,
                    data: {
                        'csrfmiddlewaretoken': myGlobal.csrfmiddlewaretoken,
                        'pk': pk,
                        'status': status,
                    },
                    success: function (response) {
                        console.log(response);
                    },
                    error: function (request, status, error) {
                        alert("로그인이 필요합니다!")
                        window.location.replace("/accounts/login/")
                    }
                })
            }
        }
    });
    $(".mv_zone .item-area").disableSelection();
});