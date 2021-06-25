$("#get_esm_data").click(function (){
   const url = 'ajax/get_spouse_info';
   const s_esm_no = $("#id_spouse_esm_no").val();
    $.ajax({
            url: url,
            data: {
                    's_esm_no': s_esm_no
            },
            success: function (data) {
                $('#esm_list').html(data);
            }
        });
});