/**
 * Copyright (c) 2017 AcFun, Inc. All Rights Reserved
 * @author: xuchu(xuchu@acfun.tv) on 17/3/13.
 */
$(document).ready(function(){
    var submit_info = $("select option:selected").text();
    $("#id_span_selected").append(submit_info);
    console.log(submit_info);
    $("#id_select").change(function(){ SelectChange(); });
    function SelectChange(){//获取下拉框选中项的text属性值
        var selectText = $("#id_select").find("option:selected").text();
        console.log("select被改变:" + selectText);
        $("#id_span_selected").html(selectText);
    }
});