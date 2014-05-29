$(document).ready(function(){
  $(".frm-register").hide();
  
  $(".btn-register").click(function(){
    $(".frm-register").toggle();
  });
  
    /*$(".form-signin").validate({
        description: {
            email: {
                required: '<div class="alert alert-error">The email address format is not correct</div>'
            },
            
            password: {
                required: '<div class="alert alert-error">The password is mandatory, the password can be characters, numbers and symbols.</div>'
            }
        }
    });*/
});
