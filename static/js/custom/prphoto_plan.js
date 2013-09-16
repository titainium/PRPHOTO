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
        var initiator = $("#initiator-list").val();
        
        if (initiator.length == 0) {
            $("#initiator-list").attr("value", $("#initiators").val());
        } else {
            initiator += "," + $("#initiators").val();
            $("#initiator-list").attr("value", initiator);
        }
    });
    
    $("#initiator-lists").delegate(".initiator", "mouseover", function(){
        $(this).css("text-decoration", "line-through");
    });
    
    $("#initiator-lists").delegate(".initiator", "mouseout", function(){
        $(this).css("text-decoration", "none");
    });
    
    $("#initiator-lists").delegate(".initiator-container", "click", function(){
        var removed_initiator = $(this).text();
        var removed_position = $("#initiator-list").val().indexOf(removed_initiator);
        var sub_initiator = $("#initiator-list").val().substring(0, removed_position);
        if ($("#initiator-list").val().indexOf(",") == -1) {
            var sub_next = $("#initiator-list").val().substr(removed_position + removed_initiator.length);
        } else if ($("#initiator-list").val().length == removed_position + removed_initiator.length) {
            var sub_next = $("#initiator-list").val().substr(removed_position - 1 + removed_initiator.length);
        } else {
            var sub_next = $("#initiator-list").val().substr(removed_position + 1 + removed_initiator.length);
        }
        $("#initiator-list").attr("value", sub_initiator + sub_next);
        $(this).remove();
    });
    
    $("#masters").marcoPolo({
        url: "/plan/check_user",
        param: "nick_name",
        formatItem: function(data, $item) {
            return data;
        },
        onSelect: function(data, $item) {
            this.val(data);
        }
    });
    
    $("#add-masters").click(function(){
        $("#master-lists").append("<span class='master-container'><span class='label master'>" + $("#masters").val() + "</span>&nbsp;</span>");
        var master = $("#master-list").val();
        
        if (master.length == 0) {
            $("#master-list").attr("value", $("#masters").val());
        } else {
            master += "," + $("#masters").val();
            $("#master-list").attr("value", master);
        }
    });
    
    $("#master-lists").delegate(".master", "mouseover", function(){
        $(this).css("text-decoration", "line-through");
    });
    
    $("#master-lists").delegate(".master", "mouseout", function(){
        $(this).css("text-decoration", "none");
    });
    
    $("#master-lists").delegate(".master-container", "click", function(){
        var removed_master = $(this).text();
        var removed_position = $("#master-list").val().indexOf(removed_master);
        var sub_master = $("#master-list").val().substring(0, removed_position);
        if ($("#master-list").val().indexOf(",") == -1) {
            var sub_next = $("#master-list").val().substr(removed_position + removed_master.length);
        } else if ($("#master-list").val().length == removed_position + removed_master.length) {
            var sub_next = $("#master-list").val().substr(removed_position - 1 + removed_master.length);
        } else {
            var sub_next = $("#master-list").val().substr(removed_position + 1 + removed_master.length);
        }
        $("#master-list").attr("value", sub_master + sub_next);
        $(this).remove();
    });
    
    $("#members").marcoPolo({
        url: "/plan/check_user",
        param: "nick_name",
        formatItem: function(data, $item) {
            return data;
        },
        onSelect: function(data, $item) {
            this.val(data);
        }
    });
    
    $("#add-members").click(function(){
        $("#member-lists").append("<span class='member-container'><span class='label member'>" + $("#members").val() + "</span>&nbsp;</span>");
        var member = $("#member-list").val();
        
        if (member.length == 0) {
            $("#member-list").attr("value", $("#members").val());
        } else {
            member += "," + $("#members").val();
            $("#member-list").attr("value", member);
        }
    });
    
    $("#member-lists").delegate(".member", "mouseover", function(){
        $(this).css("text-decoration", "line-through");
    });
    
    $("#member-lists").delegate(".member", "mouseout", function(){
        $(this).css("text-decoration", "none");
    });
    
    $("#member-lists").delegate(".member-container", "click", function(){
        var removed_member = $(this).text();
        var removed_position = $("#member-list").val().indexOf(removed_member);
        var sub_member = $("#member-list").val().substring(0, removed_position);
        if ($("#member-list").val().indexOf(",") == -1) {
            var sub_next = $("#member-list").val().substr(removed_position + removed_member.length);
        } else if ($("#member-list").val().length == removed_position + removed_member.length) {
            var sub_next = $("#member-list").val().substr(removed_position - 1 + removed_member.length);
        } else {
            var sub_next = $("#member-list").val().substr(removed_position + 1 + removed_member.length);
        }
        $("#member-list").attr("value", sub_member + sub_next);
        $(this).remove();
    });
    
    $("#add-equipments").click(function(){
        $("#equipment-lists").append("<span class='equipment-container'><span class='label equipment'>" + $("#equipments").val() + "</span>&nbsp;</span>");
        var equipment = $("#equipment-list").val();
        
        if (equipment.length == 0) {
            $("#equipment-list").attr("value", $("#equipments").val());
        } else {
            equipment += "," + $("#equipments").val();
            $("#equipment-list").attr("value", equipment);
        }
    });
    
    $("#equipment-lists").delegate(".equipment", "mouseover", function(){
        $(this).css("text-decoration", "line-through");
    });
    
    $("#equipment-lists").delegate(".equipment", "mouseout", function(){
        $(this).css("text-decoration", "none");
    });
    
    $("#equipment-lists").delegate(".equipment-container", "click", function(){
        var removed_equipment = $(this).text();
        var removed_position = $("#equipment-list").val().indexOf(removed_equipment);
        var sub_equipment = $("#equipment-list").val().substring(0, removed_position);
        if ($("#equipment-list").val().indexOf(",") == -1) {
            var sub_next = $("#equipment-list").val().substr(removed_position + removed_equipment.length);
        } else if ($("#equipment-list").val().length == removed_position + removed_equipment.length) {
            var sub_next = $("#equipment-list").val().substr(removed_position - 1 + removed_equipment.length);
        } else {
            var sub_next = $("#equipment-list").val().substr(removed_position + 1 + removed_equipment.length);
        }
        $("#equipment-list").attr("value", sub_equipment + sub_next);
        $(this).remove();
    });
    
    $(":button").click(function(){
        if ($(this).attr("value") == "next") {
            $("#" + $(this).attr("prev")).slideUp();
            $("#" + $(this).attr("next")).slideDown();
        } else if ($(this).attr("value") == "prev") {
            $("#" + $(this).attr("next")).slideUp();
            $("#" + $(this).attr("prev")).slideDown();
        }
    });
    
    $(".title-unit, .members-unit, description-unit, misc-unit").tooltip({placement: 'top',
        title: 'Edit'
    });
});
