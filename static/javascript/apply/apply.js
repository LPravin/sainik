function hideeveything(){
        $('#div_id_esm_no').attr("hidden", true);
        $('#div_id_zsb').attr("hidden", true);
        $('#div_id_esm_reg_type').attr("hidden", true);
    $('#div_id_service').attr("hidden", true);
    $('#div_id_corps').attr("hidden", true);
    $('#div_id_record_office').attr("hidden", true);
    $('#div_id_group').attr("hidden", true);
    $('#div_id_expiry_date').attr("hidden", true);
    $('#div_id_trade').attr("hidden", true);
    $('#div_id_rank_category').attr("hidden", true);
    $('#div_id_rank').attr("hidden", true);
    $('#div_id_service_no').attr('hidden', true);
    $('#div_id_state').attr("hidden", true);
    $('#div_id_district').attr("hidden", true);
    $('#div_id_discharge_book').attr("hidden", true);
    $('#div_id_ppo_book').attr("hidden", true);
    $('#div_id_death_certificate').attr("hidden", true);
    $('#div_id_residence_certificate').attr("hidden", true);
    $(".textinput").val("");
    }
    function showesm(){
        $('#div_id_esm_reg_type').attr("hidden", false);
    $('#div_id_service').attr("hidden", false);
    $('#div_id_record_office').attr("hidden", false);
    $('#div_id_group').attr("hidden", false);
    $('#div_id_trade').attr("hidden", false);
    $('#div_id_rank_category').attr("hidden", false);
    $('#div_id_rank').attr("hidden", false);
    $('#div_id_service_no').attr("hidden", false);
    $('#div_id_state').attr("hidden", false);
    $('#div_id_district').attr("hidden", false);
    $('#div_id_discharge_book').attr("hidden", false);
    $('#div_id_ppo_book').attr("hidden", false);
    $('#div_id_residence_certificate').attr("hidden", false);
    }
    function showunregwidow(){
        $('#div_id_expiry_date').attr("hidden", false);
        $('#div_id_death_certificate').attr("hidden", false);
    }
    function showregwidow(){
        $('#div_id_esm_no').attr("hidden", false);
        showunregwidow();
    }
    function showtransesm(){
        $('#div_id_esm_no').attr("hidden", false);
        $('#div_id_zsb').attr("hidden", false);
        showesm();
    }

    $('#id_basic_reg_type').change(function (){
         hideeveything();
        if ($(this).val() === 'E'){
        showesm();
        } else if ($(this).val() === 'W'){
        showregwidow();
            $('#div_id_esm_no').attr('required', 'required');
        } else if ($(this).val() === 'TE'){
            showtransesm();
        } else if ($(this).val() === 'TW'){
            showtransesm();
        } else if ($(this).val() === 'UW'){
            showunregwidow();
            showesm();
        }

    }).trigger('change');
    $("#id_service").change(function () {
        const url = $("#applyform").attr("data-records-url");
        const serviceid = $(this).val();
        $.ajax({
            url: url,
            data: {
                'service_id': serviceid
            },
            success: function (data) {
                $("#id_record_office").html(data);
            }
        });
        if(serviceid === '2'){
            $("#div_id_corps").attr('hidden',false);
        }
        else
        {
            $("#div_id_corps").attr('hidden',true);
        }
        if($("#id_group").val() !=="") {
            const urll = $("#applyform").attr("data-trades-url");
            const groupid = $('#id_group').val();

            $.ajax({
                url: urll,
                data: {
                    'service_id': serviceid,
                    'groupid': groupid
                },
                success: function (data) {
                    $("#id_trade").html(data);

                }
            });
        }
        if($("#id_rank_category").val() !== '') {
            const urlll = $("#applyform").attr("data-ranks-url");
            const rankcatid = $('#id_rank_category').val();

            $.ajax({
                url: urlll,
                data: {
                    'service_id': serviceid,
                    'rankcatid': rankcatid
                },
                success: function (data) {
                    $("#id_rank").html(data);

                }
            });
        }
    });
    $("#id_group").change(function (){
        const url = $("#applyform").attr("data-trades-url");
        const groupid = $(this).val();
        const serviceid = $("#id_service").val();

        $.ajax({
            url: url,
            data: {
                'service_id': serviceid,
                 'groupid' :  groupid
            },
            success: function (data) {
                $("#id_trade").html(data);

            }
        });
    });
    $("#id_rank_category").change(function () {
        const url = $("#applyform").attr("data-ranks-url");
        const rankcatid = $(this).val();
        const serviceid = $("#id_service").val();

        $.ajax({
            url: url,
            data: {
                'service_id': serviceid,
                 'rankcatid' :  rankcatid
            },
            success: function (data) {
                $("#id_rank").html(data);

            }
        });

    });
    $("#id_state").change(function getdistricts() {
        const url = $("#applyform").attr("data-districts-url");
        const stateid = $(this).val();

        $.ajax({
            url: url,
            data: {
                'stateid': stateid
            },
            success: function (data) {
                $("#id_district").html(data);
            }
        });
    });
    $(document).ready(function(){
        hideeveything();

    });
    function details(evt, tabName) {

  var i;
  var x = document.getElementsByClassName("tab");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  document.getElementById(tabName).style.display = "block";
}

     document.getElementById("defaultOpen").click();
    // function validateForm() {
    //   // This function deals with validation of the form fields
    //   var x, y, i, valid = true;
    //   x = document.getElementsByClassName("tab");
    //   y = x[currentTab].getElementsByTagName("input");
    //   // A loop that checks every input field in the current tab:
    //   for (i = 0; i < y.length; i++) {
    //     // If a field is empty...
    //     if (y[i].value == "") {
    //       // add an "invalid" class to the field:
    //       y[i].className += " invalid";
    //       // and set the current valid status to false
    //       valid = false;
    //     }
    //   }