$(document).ready(function(){
  $(".frm-register").hide();
  $("#loginModal").modal('show');
  
  $(".btn-register").click(function(){
    $(".frm-register").toggle();
  });
});
