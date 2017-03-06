/**
 * Copyright (c) 2017 AcFun, Inc. All Rights Reserved
 * @author: xuchu(xuchu@acfun.tv) on 17/3/6.
 */
$(document).ready(function(){
            var h_th_1 = $('#id_tbody').offset().top;
            var w_table = $("table").find("tr").width() + 30;
            $('#ssh_result').offset({ top: h_th_1});
            $('#ssh_result').offset({ left: w_table});

            $.ajaxSetup({
                 data: {csrfmiddlewaretoken: '{{ csrf_token }}' }
            });
            $('.btn-sm').click(function(){
                var btn_text = $(this).attr("name");
                console.log(btn_text);
                var c_time = new Date();
                $('#ssh_result').html("<kbd>执行开始于[" + c_time.toLocaleString() + "]</kbd><br>");
                $.ajax({
                    url: "/ssh_qa_runshell/",
                    type:"POST",
                    crossDomain:true,
                    xhrFields:{withCredentials:true},
                    data: {"btn_text":btn_text},
                    cache: false
                }).done(function(ajax_req){
                        $('#ssh_result').append("<kbd>Action[" + btn_text + "]</kbd><br>" + ajax_req)}).fail(function(e){
                       $('#ssh_result').html(e)
                });
                $('body,html').animate({ scrollTop: 0 }, 100);

                });
            });