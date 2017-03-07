/**
 * Copyright (c) 2017 AcFun, Inc. All Rights Reserved
 * @author: xuchu(xuchu@acfun.tv) on 17/3/6.
 */
$(document).ready(function(){
    var body_width = document.body.clientWidth;
    var h_th_1 = $('#table').offset().top;
    var w_table = $("table").find("tr").width() + 30;
    $('#ssh_front_result').offset({ top: h_th_1});
    $('#ssh_front_result').offset({ left: w_table});
    $('#ssh_front_result').css({
        "width":body_width-w_table
    });
    console.log(body_width-w_table)

});//JS end