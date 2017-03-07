/**
 * Copyright (c) 2017 AcFun, Inc. All Rights Reserved
 * @author: xuchu(xuchu@acfun.tv) on 17/3/6.
 */
$(document).ready(function(){
    var h_th_1 = $('#id_tbody').offset().top;
    var w_table = $("table").find("tr").width() + 30;
    $('#ssh_result').offset({ top: h_th_1});
    $('#ssh_result').offset({ left: w_table});

});//JS end