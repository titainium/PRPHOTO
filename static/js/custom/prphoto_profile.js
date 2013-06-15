$(document).ready(function(){
    $("#edit_nickname").click(function(){
      var cell = $(this).parents('tr').children('td');
      var nick_name = cell.eq(1).text();
      cell.eq(1).html("<input type='text' id='nick_name' class='span2' name='nick_name' value='" + nick_name + "' />");
      cell.eq(2).html("&nbsp;&nbsp;<a href='#' id='submit_nickname'>save</a>");
    });
    
    $("#btn_nickname").delegate("a", "click", function() {
      var cell = $("#btn_nickname").parents('tr').children('td');
      
      $.post("/update_profile",
             {nick_name: $("#nick_name").val()},
             function(data) {
               cell.eq(1).html(data);
               cell.eq(2).html("&nbsp;&nbsp;<a href='#' id='edit_nickname'>edit</a>");
             }
            );
    });
    
    $("#edit_location").click(function(){
      var cell = $(this).parents('tr').children('td');
      var location = cell.eq(1).text();
      cell.eq(1).html("<input type='text' id='location' class='span2' name='location' value='" + location + "' />");
      cell.eq(2).html("<a href='#' id='submit_location'>save</a>");
    });
    
    $("#btn_location").delegate("a", "click", function() {
      var cell = $(this).parents('tr').children('td');
      var location = $(this).parents('tr').children('td').eq(1).text();
      $.post("/update_profile",
             {location: location},
             function(data) {
               cell.eq(1).html(data);
               cell.eq(2).html("&nbsp;&nbsp;<a href='#' id='edit_location'>edit</a>");
             }
            );
    });
});
