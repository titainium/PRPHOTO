$(document).ready(function(){
    $("#btn_nickname").delegate("#edit_nickname", "click", function(){
      var cell = $("#btn_nickname").parents('tr').children('td');
      var nickname = cell.eq(1).text();
      cell.eq(1).html("<input type='text' id='nickname' class='span2' name='nickname' value='" + nickname + "' />");
      cell.eq(2).html("&nbsp;&nbsp;&nbsp;<a href='#' id='submit_nickname'>save</a>");
    });
    
    $("#btn_nickname").delegate("#submit_nickname", "click", function() {
      var cell = $("#btn_nickname").parents('tr').children('td');
      
      $.post("/update_profile",
             {nickname: $("#nickname").val()},
             function(data) {
               cell.eq(1).html(data);
               cell.eq(2).html("&nbsp;&nbsp;&nbsp;<a href='#' id='edit_nickname'>edit</a>");
             }
            );
    });
    
    $("#btn_location").delegate("#edit_location", "click", function(){
      var cell = $("#btn_location").parents('tr').children('td');
      var location = cell.eq(1).text();
      cell.eq(1).html("<input type='text' id='location' class='span2' name='location' value='" + location + "' />");
      cell.eq(2).html("&nbsp;&nbsp;&nbsp;<a href='#' id='submit_location'>save</a>");
    });
    
    $("#btn_location").delegate("#submit_location", "click", function() {
      var cell = $("#btn_location").parents('tr').children('td');
      $.post("/update_profile",
             {location: $("#location").val()},
             function(data) {
               cell.eq(1).html(data);
               cell.eq(2).html("&nbsp;&nbsp;&nbsp;<a href='#' id='edit_location'>edit</a>");
             }
            );
    });
    
    $("#btn_password").delegate("#edit_password", "click", function(){
      var cell = $("#btn_password").parents('tr').children('td');
      var password = cell.eq(1).text();
      cell.eq(1).html("<input type='password' id='password' class='span2' name='password' value='" + password + "' />");
      cell.eq(2).html("&nbsp;&nbsp;&nbsp;<a href='#' id='submit_password'>save</a>");
    });
    
    $("#btn_password").delegate("#submit_password", "click", function() {
      $('#password-modal').modal('show');
    });
    
    $(".save-password").click(function(){
      var cell = $("#btn_password").parents('tr').children('td');
      $.post("/update_user",
             {password: $("#password").val()},
             function(data) {
               cell.eq(1).html(data);
               cell.eq(2).html("&nbsp;&nbsp;&nbsp;<a href='#' id='edit_password'>edit</a>");
             }
            );
    });
    
    $('#password-modal').modal('hide');
});
