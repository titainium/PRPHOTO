$(document).ready(function(){
    $('#tags').tagsInput();
    
    $("#initiators").marcoPolo({
        url: "/plan/check_user",
        param: "nick_name",
        formatItem: function(data, $item) {
            return data;
        },
        onSelect: function(data, $item) {
            this.val(data);
        }
    });
    
    $("#add-initiators").click(function(){
        $("#initiator-lists").append("<span class='initiator-container'><span class='label initiator'>" + $("#initiators").val() + "</span>&nbsp;</span>");
    });
    
    $("#initiator-lists").delegate(".initiator", "mouseover", function(){
        $(this).css("text-decoration", "line-through");
    });
    
    $("#initiator-lists").delegate(".initiator", "mouseout", function(){
        $(this).css("text-decoration", "none");
    });
    
    $("#initiator-lists").delegate(".initiator-container", "click", function(){
        $(this).remove();
    });
});
