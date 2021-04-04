
        const email= document.getElementById("id_email")
        const password1 = document.getElementById("id_password1")
        const password2 = document.getElementById("id_password2")
        const name = document.getElementById("id_name");
        const mobile = document.getElementById("id_mobile")
        const ert = document.getElementById("id_esm_reg_type");
        const service = document.getElementById("id_service");
        const rank = document.getElementById("id_rank");
        const ro = document.getElementById("id_record_office");
        const sno = document.getElementById("id_service_no");
        const group = document.getElementById("id_group");
        const trade = document.getElementById("id_trade");
        const rcat = document.getElementById("id_rank_category");
        const esm_no = document.getElementById("id_esm_no");

        $("#id_service").change(function () {
        const url = $("#addesmform").attr("data-records-url");
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
            const urll = $("#addesmform").attr("data-trades-url");
            const groupid = $('#id_group').val();

            $.ajax({
                url: urll,
                data: {
                    'service_id': serviceid,
                    'groupid': groupid
                },
                success: function (data) {
                    $("#id_trade").html(data);
                    // $('#id_rank').html(<option value="">Select rank category</option>);
                    // $('#id_trade').html(<option value="">Select trade</option>);
                }
            });
        }
        if($("#id_rank_category").val() !== '') {
            const urlll = $("#addesmform").attr("data-ranks-url");
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
        const url = $("#addesmform").attr("data-trades-url");
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
        const url = $("#addesmform").attr("data-ranks-url");
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
        const url = $("#addesmform").attr("data-districts-url");
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
    function alphaOnly(event) {
  let key = event.keyCode;
  return ((key >= 65 && key <= 90) || key === 8);
    }

    function numOnly(event) {
    let key = event.keyCode;
  return ((key >= 48 && key <= 57) || (key >= 96 && key <= 105) || key === 8);
    }
$(document).ready(function(){
    $('#div_id_corps').attr("hidden", true);
    $("#id_reg_date").attr("max", 0)
    // $('#id_enrollment_date').attr("min", {{ date }})
});
function validateform() {
   // if (ert.value === ""){
   //    alert("Please select ESM registration type")
   //    ert.focus();
   //    return false;
   // }
   // if (esm_no.value === ""){
   //    alert("Please fill ESM Number");
   //    service.focus();
   //    return false;
   // }
   // if (service.value === "") {
   //    alert("Please select service");
   //    service.focus();
   //    return false;
   // }
   // if (ro.value === "") {
   //    alert("Please select record office");
   //    ro.focus();
   //    return false;
   // }
   // if (group.value === "") {
   //    alert("Please select group");
   //    group.focus();
   //    return false;
   // }
   // if (trade.value === "") {
   //    alert("Please select trade");
   //    trade.focus();
   //    return false;
   // }
   // if (rcat.value === "") {
   //    alert("Please select rank category");
   //    rcat.focus();
   //    return false;
   // }
   // if (rank.value === "") {
   //    alert("Please select rank");
   //    rank.focus();
   //    return false;
   // }
   // if (sno.value === "") {
   //    alert("Please fill service number");
   //    sno.focus();
   //    return false;
   // }
   // email.value = sno.value + "@sainik.com"
   // password1.value = mobile.value
   // password2.vaue = mobile.value
   return true;
}