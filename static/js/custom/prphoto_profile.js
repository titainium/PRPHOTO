$(document).ready(function(){
    $("#edit_nickname").click(function(){
      var cell = $(this).parents('tr').children('td');
      var nick_name = cell.eq(1).text();
      cell.eq(1).html("<input type='text' id='nick_name' class='span2' name='nick_name' value='" + nick_name + "' />");
      $(this).html("<a href='#' id='submit_nickname'>save</a>");
    });
    
    $("#submit_nickname").click(function() {
      var nick_name = $(this).parents('tr').children('td').eq(1).text();
      $.ajax({
        type: "Post",
        url: "/update_profile",
        data: "{'nick_name': '" + nick_name + "'}",
        contentType: "application/json;charset=utf-8",
        dataType: "json",
        success: function(data) {
          $(this).parents('tr').children('td').eq(1).html(data);
          $(this).parents('tr').children('td').eq(2).html("&nbsp;&nbsp;<a href='#' id='edit_nickname'>edit</a>");
        },
      });
    });
    
    /*$("#submit_nickname").click(function(){
      $("form").submit();
    });*/
});
