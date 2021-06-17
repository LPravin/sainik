function load_esm_list(){
   const url = 'ajax/load_esm_list';
        $.ajax({
            url: url,
            success: function (data) {
                $('#esm_list').html(data);
            }
        });
    }
$("#search").click(function (){
   const url = 'ajax/search_esm';
   const search_input = $("#search_input").val();
   const sb = $("#search_by").val();
    $.ajax({
            url: url,
            data: {
                    'sb': sb,
                    'search_input': search_input
            },
            success: function (data) {
                $('#esm_list').html(data);
            }
        });
});
$(document).ready(function(){
load_esm_list();
 });