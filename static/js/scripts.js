$(function () {
  $(".item-area").draggable({ revert: 'invalid' });

  $(".mv_zone").droppable({
    accept: '.item-area',
    drop: function (event, ui) {
      $(this).append($(ui.helper));
      $(".item-area").addClass("item");
      $(".item").removeAttr("style");
      $(".item").draggable({
        revert: 'invalid'
      });
    }
  });

  // $(".item-area").bind("dragstart", function (event, ui) {
  //   $(this).css({
  //     'background': 'rgba(49, 217, 228, 0.3)'
  //   })
  // })
  // $(".item-area").bind("dragstop", function (event, ui) {
  //   $(this).css({
  //     'background': ''
  //   })
  // })
});
// $(".area_zone").sortable({
//   connectWith: ".area_zone",
//   handle: ".item-area",
//   placeholder: ".area_zone"
// });
// $(".ns-area").disableSelection();
// $('.item-area').draggable({
//   containment: ".todo-area",
//   stack: ".item-area",
// })


