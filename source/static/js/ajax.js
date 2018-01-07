/**
 * Created by Kiradle on 2018-1-5.
 */
function do_ajax(){
    word = $("#search").val();
    if(word!=''){
        $.get("/search", {"word": word}, function(data){
            var cc_str = '';
            var c_str = '';
            if(data.message!=[]){
                $.each($.parseJSON(data), function (k, v){
                    if(v.model=='common.careercourse'){
                        cc_str += '<a href="'+v.fields.market_page_url+'" style="background-color:#'+v.fields.course_color+';">'+v.fields.name+'</a>';
                    }else if(v.model == 'common.course'){
                        console.log(v.fields.name);
                        c_str += '<a href="'+v.fields.market_page_url+'" style="background-color:#999999">'+v.fields.name+'</a>';
                    }
                });
                if(cc_str != '' || c_str != ''){
                    //$("#drop_down").css("display", "block");
                    $("#cc_list").html(cc_str);
                    $("#c_list").html(c_str);
                }else{
                    $("#keyword-group").css("display", "none");
                    $("#cc_list").html('');
                    $("#c_list").html('');
                }
            }
        })
    }else{
        $("#cc_list").html('');
        $("#c_list").html('');
        $("#keyword-group").css("display", "none");
    }
}