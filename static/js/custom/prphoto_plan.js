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
        $("#initiator-lists").append("<span class='label initiators-list'>" + $("#initiators").val() + "</span>");
    });
    
    $(".initiators-list").hover(function(){
        $(this).css('text-decoration', 'line-through');
    });
});
