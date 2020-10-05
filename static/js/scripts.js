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

        $(document).on('click', '.update', function(e){
        e.preventDefault();
        var target = e.target;
        var origin = $(target).parent();
        var originClone = $(origin).children().clone();
        var originTitle = $(origin).children('.title')[0].innerText;
        var originContent = $(origin).children('.content')[0].innerText;
        console.log(origin, originClone, originTitle, originContent)
        /*
        $.ajax({
            type: 'GET',
            url: `${$(target).attr('href')}`,
            success: function (response) {
                console.log(response)
            }
        })*/
        var html = `
            <form action="" method="POST" class="submit_form">
                <input type="hidden" name="csrfmiddlewaretoken" value="${myGlobal.csrfmiddlewaretoken}">
                <div class="contents">
                    <div class="title RS_IP">
                        <label for="id_title" class="title_text">제목</label>
                        <input type="text" name="title" value="${originTitle}" maxlength="30" required id="id_title">
                    </div>
                    <div class="contents">
                        <label for="id_content" class=" contents_text">할 일</label>
                        <textarea name="content" cols="40" rows="10" id="id_content">${originContent}</textarea>
                    </div>
                </div>
                <div class="toDoList_Check">

                    <div class="is_progressed">
                        <label for="id_is_progressed">진행 중</label>
                        <input type="checkbox" name="is_progressed" id="id_is_progressed">
                        <br />
                        <label for="id_is_completed">완료</label>
                        <input type="checkbox" name="is_completed" id="id_is_completed">
                    </div>

                </div>
                <a href="javascript:void(0)" class="btn btn-outline-primary btn_cancel">취소</a>
                <input type="submit" value="작성">
            </form>`;

        $(origin).empty().append(html);
        $(document).on('click', '[class*=btn_cancel]', function () {
            $(origin).empty().append(originClone);
        });
        $(document).on('submit', '.submit_form', function (e) {
            e.preventDefault();
            e.stopPropagation();
            var target = e.target;
            var id = $(target).parents('.item-area').data('no');
            var formData = $(this).serialize();

            $.ajax({
                type: "POST",
                url: `${myGlobal.url}update/${id}/`,
                data: formData,
                success: function (response) {
                    $("html").html(response);
                }
            });
        });
    });
});