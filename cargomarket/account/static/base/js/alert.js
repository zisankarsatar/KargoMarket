window.setTimeout(function() {
    $(".alert-content").fadeTo(100, 0).slideUp(300, function(){
        $(this).remove(); 
    });
}, 4000);