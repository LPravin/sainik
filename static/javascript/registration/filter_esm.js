function load_esm_list(){
   const url = 'ajax/filter_esm_list';
        $.ajax({
            url: url,
            success: function (data) {
                $('#esm_list').html(data);
            }
        });
    }
$("#filter").click(function (){
    const url = 'ajax/filter_esm';
    const name = $('#id_name').val();
    const rc = $('#id_reg_category').val();
    const rcat = $('#id_rank_category').val();
    const ro = $('#id_record_office').val();
    const sj = $('#id_security_job').val();
    const service = $('#id_service').val();
    const trade = $('#id_trade').val();
    const cq = $('#id_civil_qualification').val();
    const es = $('#id_employment_status').val();
    $.ajax({
            url: url,
            data: {
                'name': name,
                'rc': rc,
                'rcat': rcat,
                'ro': ro,
                'sj': sj,
                'service': service,
                'trade': trade,
                'cq': cq,
                'es': es
            },
            success: function (data) {
                $('#esm_list').html(data);
            }
        });
});
$("#export").click(function (){
    const url = 'ajax/export_filtered_esm';
    $.ajax({
            url: url,
            data: {

            },
            success: function (data) {

            }
        });
});
$(document).ready(function(){
load_esm_list();
 });