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
    $('#div_id_discharge_book').attr("hidden", true);
    $('#div_id_ppo_book').attr("hidden", true);
    $('#div_id_death_certificate').attr("hidden", true);
    $('#div_id_residence_certificate').attr("hidden", true);
    $(".form-control").val("");
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
         const form_fields = document.getElementsByClassName('form-0')
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
        $("#id_basic_reg_type").removeClass("form-control");
        $('[name="csrfmiddlewaretoken"]').removeClass("form-control");
        hideeveything();
    });
        const brt = document.getElementById("id_basic_reg_type");
        const name = document.getElementById("id_name");
        const ert = document.getElementById("id_esm_reg_type");
        const service = document.getElementById("id_service");
        const ro = document.getElementById("id_record_office");
        const sno = document.getElementById("id_service_no");
        const group = document.getElementById("id_group");
        const trade = document.getElementById("id_trade");
        const rcat = document.getElementById("id_rank_category");
        const rank = document.getElementById("id_rank");
        const state = document.getElementById("id_state");
        const district = document.getElementById("id_district");
        const esm_no = document.getElementById("id_esm_no");
        const expiry_date = document.getElementById("id_expiry_date");
        const zsb = document.getElementById("id_zsb");

function alphaOnly(event) {
  let key = event.keyCode;
  return ((key >= 65 && key <= 90) || key === 8);
    }

    function numOnly(event) {
    let key = event.keyCode;
  return ((key >= 48 && key <= 57) || (key >= 96 && key <= 105) || key === 8);
    }

    function validateform()
    {

        if( name.value === "" ) {
           alert( "Please provide your name!" );
           name.focus();
           return false;
         }
        if (brt.value === "")
        {
            alert( "Please select basic registration type" );
            brt.focus();
            return false;
        }
        if (brt.value === "E" || brt.value === "TE" || brt.value ==="UW")
        {
            if( ert.value === ""){
                alert( "Please select ESM registration type" );
            ert.focus();
            return false;}
            if( service.value === ""){
                alert("Please select service");
                service.focus();
                return false;}
            if(ro.value === ""){
                alert("Please select record office");
                ro.focus();
            return false;}
            if(group.value  === "") {
                alert("Please select group");
                group.focus();
            return false;}
            if(trade.value  === "") {
                alert("Please select trade");
                trade.focus();
            return false;}
            if(rcat.value  === "") {
                alert("Please select rank category");
                rcat.focus();
            return false;}
            if(rank.value  === "") {
                alert("Please select rank");
                rank.focus();
            return false;}
            if(sno.value  === "") {
                alert("Please fill service number");
                sno.focus();
                return false;}
        }
        if (brt.value === "W"  || brt.value === "UW"){
             if(esm_no.value  === "") {
                alert("Please enter ESM No");
                esm_no.focus();
                return false;}
            if(expiry_date.value  === "") {
                alert("Please enter Expiry Date");
                expiry_date.focus();
                return false;}
        }
        if (brt.value === "TE"){
            if(esm_no.value  === "")
             {
                 alert("Please enter ESM registration number");
                 esm_no.focus();
                 return false;
             }
            if(zsb.value  === "")
             {
                 alert("Please Select Previous ZSB name");
                 zsb.focus();
                 return false;
             }
        }
        if (state.value === ""){
                alert("Please Select the state you want to apply");
                 state.focus();
                 return false;
        }
        if (district.value === ""){
                alert("Please Select the state you want to apply");
                 district.focus();
                 return false;
        }

        return true;

    }
