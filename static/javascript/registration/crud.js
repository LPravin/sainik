function load_esm_list(){
   const url = 'ajax/load_esm_list';
        $.ajax({
            url: url,
            success: function (data) {
                $('#esm_list').html(data);
            }
        });
    }
$(document).ready(function(){
load_esm_list();
 });