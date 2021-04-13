
function alphaOnly(event) {
  let key = event.keyCode;
  return ((key >= 65 && key <= 90) || key === 8);
    }

    function numOnly(event) {
    let key = event.keyCode;
  return ((key >= 48 && key <= 57) || (key >= 96 && key <= 105) || key === 8);
    }


    function hidepensioner(){
        $('#div_id_ppo_no').attr('hidden', true);
        $('#div_id_pension_sanctioned').attr('hidden', true);
        $('#div_id_present_pension').attr('hidden', true);
        $('#div_id_whether_pwd').attr('hidden', true);
        $('#div_id_disability_pension').attr('hidden', true);
        $('#div_id_disability_percent').attr('hidden', true);
    }
    function showpensioner(){
    $('#div_id_ppo_no').attr('hidden', false);
        $('#div_id_pension_sanctioned').attr('hidden', false);
        $('#div_id_present_pension').attr('hidden', false);
    }
    function showpwd(){
        $('#div_id_disability_pension').attr('hidden', false);
        $('#div_id_disability_percent').attr('hidden', false);
    }
    function hidepwd(){
        $('#div_id_disability_pension').attr('hidden', true);
        $('#div_id_disability_percent').attr('hidden', true);
    }

    $('#id_pensioner_status').change(function (){
       if ($(this).val() === 'Y'){
        showpensioner();
        }
       else{
           hidepensioner();
       }
       $('#div_id_whether_pwd').attr('hidden', false);
    });
$('#id_whether_pwd').change(function () {
    if ($(this).val() === 'Y') {
        showpwd();
    } else {
        hidepwd();
    }
});

     $(document).ready(function(){
        hidepensioner();
     });