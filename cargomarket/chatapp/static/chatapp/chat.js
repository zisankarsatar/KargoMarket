

function me_message(message, message_time) {
    var f_message = '<li class="chat-right"><div class="chat-hour">' + message_time;
    f_message += '<span class="fa fa-check-circle"></span></div><div class="chat-text">' + message + '</div>';
    f_message += '<div class="chat-avatar"><img src="https://www.bootdey.com/img/Content/avatar/avatar5.png" alt=""><div class="chat-name">You</div></div></li>';
    return f_message
}
function friend_message(message, message_time) {
    var Dateobj = new Date();
    var f_message = '<li class="chat-left">';
    f_message += '<div class="chat-avatar"><img src="https://www.bootdey.com/img/Content/avatar/avatar3.png"/><div class="chat-name">'+ active_chat_user_name +'</div></div>';            
    f_message += '<div class="chat-text">' + message + '</div>';
    f_message += '<div class="chat-hour">' + message_time + '<span class="fa fa-check-circle"></span></div>';
    f_message += '</li>';
    return f_message
}

function write_messages_to_panel(messages){
    messages.messages.forEach(element => {
        if (element.sender == current_user_id){
            message_text = me_message(element.message_text, element.send_time);

        } else {
            message_text = friend_message(element.message_text, element.send_time);
        }
        $(".chat-box").append(message_text);
        $(".chat-container").get(0).scrollTop += 9999;
    });
}

function select_chat(chat_id) {
    $(".active-user").removeClass("active-user");
    $("li[data-chat-id="+chat_id+"]").addClass("active-user");
    show_chat_window();
}

function show_chat_window() {
    // Show chat window - Right panel
    active_chat_id = $(".active-user").data("chatId");
    active_chat_user_name = $(".active-user > p > .name").text();
    active_chat_user_id = parseInt($(".active-user > p > span.id").text());
    $("#selected-user").text(active_chat_user_name);
    $("#no-chat-window").hide();
    $("#chat-window").show();

    $(".chat-box").empty();
    // LOAD MESSAGES FROM CHAT
    load_message(active_chat_id);
    open_websocket();
}

$(".person").on("click", function(){
    $(".active-user").removeClass("active-user");
    $(this).addClass("active-user");

    show_chat_window();    
});
