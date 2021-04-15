function hideeveything() {
        $('#div_id_willing_for_job').attr("hidden", true);
        $('#div_id_security_job').attr("hidden", true);
        $('#div_id_employer').attr("hidden", true);
        $('#div_id_monthly_income').attr("hidden", true);
        $('#div_id_department').attr("hidden", true);
        $('#div_id_civil_retirement_date').attr("hidden", true);
        $('#div_id_civil_ppo_no').attr("hidden", true);
        $('#div_id_firesafety_sec_qualification').attr("hidden", true);
    }
    function showemp(){
         $('#div_id_employer').attr("hidden", false);
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
    $('#id_employment_status').change(function () {
        hideeveything();
        if ($(this).val() === 'E') {
            showemp();
        } else if ($(this).val() === 'U') {
            showunemp();
        } else if ($(this).val() === 'R') {
            showretired();
        }
    });
    $('#id_willing_for_job').change(function () {
        if ($(this).val() === 'Y') {
            $('#div_id_security_job').attr("hidden", false);
        } else if ($(this).val() === 'N') {
            hideeveything();
            $('#div_id_willing_for_job').attr("hidden", false);
        }
    });
    $(document).ready(function(){
        hideeveything();
        if ($("#id_employment_status").val() === 'E'){
            showemp();
        } else if ($("#id_employment_status").val() === 'U') {
            showunemp();
            if ($("#id_willing_for_job").val() === 'Y'){
                $('#div_id_security_job').attr("hidden", false);
            }
        } else if ($("#id_employment_status").val() === 'R') {
            showretired();
        }

    });