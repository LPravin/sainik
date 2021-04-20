        const cq= $("#id_civil_qualification")
        const specialization = $("#id_specialization")
        const estatus = $("#id_employment_status");
        const willingforjob = $("#id_willing_for_job")
        const sjob = $("#id_security_job")
        const employer = $("#id_employer");
        const income = $("#id_monthly_income");
        const dept = $("#id_department");
        const retdate = $('#id_civil_retirement_date')
        const ppono = $('#id_civil_ppo_no')
        const firesafetySecQualification = $('#id_firesafety_sec_qualification')


function hideeveything() {
        $('#div_id_willing_for_job').attr("hidden", true);
        $('#id_willing_for_job')[0].selectedIndex = 0;
        $('#div_id_security_job').attr("hidden", true);
        $("#id_security_job")[0].selectedIndex = 0;
        $('#div_id_monthly_income').attr("hidden", true);
        $('#id_monthly_income').val('');
        $('#div_id_department').attr("hidden", true);
        $('#id_department')[0].selectedIndex = 0;
        $('#div_id_civil_retirement_date').attr("hidden", true);
        $('#id_civil_retirement_date').val('');
        $('#div_id_civil_ppo_no').attr("hidden", true);
        $('#id_civil_ppo_no').val('');
        $('#div_id_firesafety_sec_qualification').attr("hidden", true);
        $('#id_firesafety_sec_qualification').val('');
        $("#div_id_specialization").attr('hidden', true);
        $("#id_specialization")[0].selectedIndex = 0;
        $("#div_id_sector").attr('hidden', true);
        $("#id_sector")[0].selectedIndex = 0;
    }
    function showemp(){
        $("#div_id_sector").attr('hidden', false);
        $('#div_id_monthly_income').attr("hidden", false);
        $('#div_id_department').attr("hidden", false);
    }
    function showunemp(){
        $('#div_id_willing_for_job').attr("hidden", false);
    }
    function showretired(){
        $('#div_id_civil_retirement_date').attr("hidden", false);
        $('#div_id_civil_ppo_no').attr("hidden", false);
    }
    estatus.change(function () {
        hideeveything();
        if ($(this).val() === 'E') {
            showemp();
        } else if ($(this).val() === 'U') {
            showunemp();
        } else if ($(this).val() === 'R') {
            showretired();
        }
    });
    willingforjob.change(function () {
        if ($(this).val() === 'Y') {
            $('#div_id_security_job').attr("hidden", false);
        } else if ($(this).val() === 'N') {
            hideeveything();
            $('#div_id_willing_for_job').attr("hidden", false);
        }
    });
    cq.change(function () {
        if (cq.val() === '4' || cq.val() === '5' ||
            cq.val() === '6' || cq.val() === '7'){
            $("#div_id_specialization").attr('hidden', false);
        }
        else{
            $("#div_id_specialization").attr('hidden', true);
        }
    });
    $(document).ready(function(){
        hideeveything();
        if (cq.val() === '4' || cq.val() === '5' ||
            cq.val() === '6' || cq.val() === '7'){
            $("#div_id_specialization").attr('hidden', false);
        }
        if (estatus.val() === 'E'){
            showemp();
        } else if (estatus.val() === 'U') {
            showunemp();
            if (willingforjob.val() === 'Y'){
                $("#div_id_security_job").attr("hidden", false);
            }
        } else if (estatus.val() === 'R') {
            showretired();
        }

    });