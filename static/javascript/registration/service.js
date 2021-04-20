
        const email= $("#id_email")
        const password1 = $("#id_password1")
        const password2 = $("#id_password2")
        const name = $("#id_name");
        const mobile = $("#id_mobile")
        const ert = $("#id_esm_reg_type");
        const service = $("#id_service");
        const rank = $("#id_rank");
        const corps = $('#id_corps');
        const ro = $("#id_record_office");
        const sno = $("#id_service_no");
        const group = $("#id_group");
        const trade = $("#id_trade");
        const rcat = $("#id_rank_category");
        const esm_no = $("#id_esm_no");
        const states = $("#id_state");
        const districts = $("#id_district");
        const edate = $("#id_enrollment_date");
        const dob = $("#id_dob");
        const esm_reg_date =$("#id_reg_date")

        dob.change(function (){
            var bdate = new Date(dob.val());
            var dd = bdate.getDate();
            var mm = bdate.getMonth() + 1;
            var yyyy = bdate.getFullYear() + 15;
            if (dd < 10) {
            dd = '0' + dd;
            }
             if (mm < 10) {
            mm = '0' + mm;
            }
           edate.attr('min',(yyyy + '-' + mm + '-' + dd));
        });
        edate.click(function (){
           if (dob.val() === ""){
               alert("Please select Date of Birth");
           }
        });

        edate.change(function (){
            var bdate = new Date(edate.val());
            var dd = bdate.getDate();
            var mm = bdate.getMonth() + 1;
            var yyyy = bdate.getFullYear() ;
            if (dd < 10) {
            dd = '0' + dd;
            }
             if (mm < 10) {
            mm = '0' + mm;
            }
           esm_reg_date.attr('min',(yyyy + '-' + mm + '-' + dd));
        });

        esm_reg_date.click(function (){
           if (edate.val() === ""){
               alert("Please select Enrollment Date");
           }
        });

        service.change(function () {
        const serviceid = $(this).val();
        if (serviceid !== '1') {
            const url = $("#addesmform").attr("data-records-url");
            $.ajax({
                url: url,
                data: {
                    'service_id': serviceid
                },
                success: function (data) {
                    ro.html(data);
                    $("#div_id_corps").attr('hidden',true);
                    corps[0].selectedIndex = 0;
                    corps.value = 0;
                }
            });
        }
        else{
            ro[0].selectedIndex = 0;
            $("#div_id_corps").attr('hidden',false);

        }

        // if($("#id_group").val() !=="") {
        //     const urll = $("#addesmform").attr("data-trades-url");
        //     const groupid = $('#id_group').val();
        //
        //     $.ajax({
        //         url: urll,
        //         data: {
        //             'service_id': serviceid,
        //             'groupid': groupid
        //         },
        //         success: function (data) {
        //             $("#id_trade").html(data);
        //             // $('#id_rank').html(<option value="">Select rank category</option>);
        //             // $('#id_trade').html(<option value="">Select trade</option>);
        //         }
        //     });
        // }
        // if($("#id_rank_category").val() !== '') {
        //     const urlll = $("#addesmform").attr("data-ranks-url");
        //     const rankcatid = $('#id_rank_category').val();
        //
        //     $.ajax({
        //         url: urlll,
        //         data: {
        //             'service_id': serviceid,
        //             'rankcatid': rankcatid
        //         },
        //         success: function (data) {
        //             $("#id_rank").html(data);
        //
        //         }
        //     });
        // }
    });
    group.change(function (){
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
                trade.html(data);

            }
        });
    });
    rcat.change(function () {
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
                rank.html(data);

            }
        });
        const ur = $("#addesmform").attr("data-prefixes-url");
        $.ajax({
            url: ur,
            data: {
                'service_id': serviceid,
                 'rankcat_id' :  rankcatid
            },
            success: function (data) {
                $("#id_prefix").html(data);
            }
        });

    });
    states.change(function () {
        const url = $("#addesmform").attr("data-districts-url");
        const stateid = $(this).val();

        $.ajax({
            url: url,
            data: {
                'stateid': stateid
            },
            success: function (data) {
                districts.html(data);
            }
        });
    });


$(document).ready(function(){
    // $("#id_reg_date").attr("max", 0)
    $("#id_name").focus();
    if ($( "#id_service option:selected").text().toUpperCase() !== 'ARMY') {
        $("#div_id_corps").attr('hidden', true);
    }
});

// function mmm() {
//      const service = $( "#id_service option:selected").text().toUpperCase();
//         if(service === 'ARMY'){
//             $("#div_id_corps").attr('hidden',false);
//         }
//         else
//         {
//             $("#div_id_corps").attr('hidden', true);
//             ro[0].selectedIndex = 1;
//             $('#id_record_office option')[1].selected = true;
//         }
// }
corps.change(function (){
     const url = $("#addesmform").attr("data-army-records-url");
        const corps_id = $(this).val();

        $.ajax({
            url: url,
            data: {
                'corps_id': corps_id
            },
            success: function (data) {
                ro.html(data);
                ro[0].selectedIndex = 1;
                ro.value = ro.index(1).val();
                // ro.val($("#id_record_office")[0].selectedIndex = 1);
            }
        });
});

ert.change(function (){
   if (servicee === "ARMY"){

   }
});