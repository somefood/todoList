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
                var obj = {}
                $('.item-area').each(function (idx, item) {
                    obj[$(item).data('no')] = idx + 1;
                })
                $.ajax({
                    type: "POST",
                    url: myGlobal.changeUrl,
                    data: {
                        'csrfmiddlewaretoken': myGlobal.csrfmiddlewaretoken,
                        'pk': pk,
                        'status': status,
                        'priority': JSON.stringify(obj)
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

    $(document).on('click', '.New, .update', function (e) {
        e.preventDefault();
        var target = e.target
        var uri = $(target).attr('href').slice(1,);
        var url = `${myGlobal.url}${uri}`

        $.ajax({
            type: "GET",
            url: url,
            success: function (response) {
                var new_arr = $.parseHTML(response)
                var src = new_arr[15].innerHTML;
                makeModal(src, url);
            },
            // async: false
        });
    });

    $(document).on('click', '.delete', function(e){
        e.preventDefault();
        var is_deleted = confirm("삭제하시겠습니까?")
        if (is_deleted) {
            var target = e.target
            var uri = $(target).attr('href').slice(1,);
            var url = `${myGlobal.url}${uri}`

            $.ajax({
                type: "POST",
                url: url,
                data: {
                    csrfmiddlewaretoken: myGlobal.csrfmiddlewaretoken
                },
                success: function (response) {
                    $(target).parents('.item-area').remove();
                },
            });
        } else {
            return false;
        }
    });

    $(document).on('click', '.close', function (e) {
        e.preventDefault();
        $('.modal').remove();
        $('.modal-con').remove();
    });

    $(document).on('submit', '.submit_form', function (e) {
        e.preventDefault();
        e.stopPropagation();
        var target = e.target;
        var url = $(target).attr('action')
        var formData = $(this).serialize();

        $.ajax({
            type: "POST",
            url: url,
            data: formData,
           success: function (response) {
                location.reload();
            }
        });
    });

    function makeModal(src, url){
        var $modal = $('<div class="modal"></div>')
        var $modalCon = $('<div class="modal-con"></div>')
        $($modalCon).append(src);
        $("body").append($modal);
        $("body").append($modalCon);
        $('.submit_form').attr('action', url);
        $('.submit_form .btn-group').append($('<a href="javascript:;" class="close btn">취소</a>'));
    }
});