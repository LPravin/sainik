function hidespouse(){
    $('#div_id_spouse_name').attr("hidden", true);
    $('#div_id_marriage_date').attr("hidden", true);
    $('#div_id_spouse_relation').attr("hidden", true);
    $('#div_id_dob').attr("hidden", true);
    $('#div_id_spouse_qualification').attr("hidden", true);
    $('#div_id_spouse_employment_status').attr("hidden", true);
    $('#div_id_spouse_profession').attr("hidden", true);
    $('#div_id_spouse_retirement_date').attr("hidden", true);
    $('#div_id_spouse_aadhaar').attr('hidden', true);
    $('#div_id_spouse_voter_id').attr("hidden", true);
    $('#div_id_spouse_pan_id').attr("hidden", true);
    $('#div_id_spouse_csd_id').attr("hidden", true);
    $('#div_id_spouse_echs_id').attr('hidden', true);
    $('#div_id_ident1').attr("hidden", true);
    $('#div_id_ident2').attr("hidden", true);
    $(".form-control").val("");
}
function showspouse(){
    $('#div_id_spouse_name').attr("hidden", false);
    $('#div_id_marriage_date').attr("hidden", false);
    $('#div_id_spouse_relation').attr("hidden", false);
    $('#div_id_dob').attr("hidden", false);
    $('#div_id_spouse_qualification').attr("hidden", false);
    $('#div_id_spouse_employment_status').attr("hidden", false);
    $('#div_id_spouse_profession').attr("hidden", false);
    $('#div_id_spouse_retirement_date').attr("hidden", false);
    $('#div_id_spouse_aadhaar').attr('hidden', false);
    $('#div_id_spouse_voter_id').attr("hidden", false);
    $('#div_id_spouse_pan_id').attr("hidden", false);
    $('#div_id_spouse_csd_id').attr("hidden", false);
    $('#div_id_spouse_echs_id').attr('hidden', false);
    $('#div_id_ident1').attr("hidden", false);
    $('#div_id_ident2').attr("hidden", false);
}




$('#id_marital_status').change(function (){
         hidespouse();
        if ($(this).val() === 'M'){
        showspouse();
        } else if ($(this).val() === 'D'){
           // showdivorced();
        } else if ($(this).val() === 'W'){
            // showwidowed();
        }

    });
 $(document).ready(function(){
     const form_fields = document.getElementsByTagName('input');
     const form_select = document.getElementsByTagName('select');
        for (let f in form_fields) {
            if(form_fields.hasOwnProperty(f)){
                form_fields[f].className = "form-control"
            }
        }
        for (let s in form_select) {
            if(form_select.hasOwnProperty(s)){
                form_select[s].className = "form-control"
            }
        }
        $("#id_next_of_kin").removeClass("form-control");
        $('#id_nok_relation').removeClass("form-control");
        $('#id_marital_status').removeClass('form-control');
        $('[name="csrfmiddlewaretoken"]').removeClass("form-control");
   hidespouse();
 });


function alphaOnly(event) {
  let key = event.keyCode;
  return ((key >= 65 && key <= 90) || key === 8);
    }

    function numOnly(event) {
    let key = event.keyCode;
  return ((key >= 48 && key <= 57) || (key >= 96 && key <= 105) || key === 8);
    }

