$(document).ready(function(){
    $('#tags').tagsInput();
    
    $("#initiators").autocomplete({
        autoFocus: true,
        source: function(request, response){
            $.ajax({type: "POST",
                   url: "/plan/check_user",
                   data: {nick_name: $("#initiators").val()},
                          contentType: "application/x-www-form-urlencoded;charset=UTF-8",
                          dataType: "json",
                          success: function(result){
                            response($.map(result, function(user){
                                return user
                            }));
                          },
                   });
            },
    });
});
