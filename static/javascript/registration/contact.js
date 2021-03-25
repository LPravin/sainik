$('#id_is_address_same').change( function () {
    if (this.checked) {
        this.value = true
        // $("#presentaddress").hide();
        $('#hno').attr({'value': $('#id_house_no').val(), 'disabled': true})
        $('#hname').attr({'value': $('#id_house_name').val(), 'disabled': true})
        $('#sname').attr({'value': $('#id_street_name').val(), 'disabled': true})
        $('#city').attr({'value': $('#id_city').val(), 'disabled': true})
        $('#district').val($('#id_district').val()).attr('disabled', true);
        $('#state').val($('#id_state').val()).attr('disabled', true);
        $('#pincode').attr({'value': $('#id_pincode').val(), 'disabled': true})
    } else {
        this.value = false
        $("#presentaddress").show();
        $('#hno').attr({'value': '', 'disabled': false})
        $('#hname').attr({'value': '', 'disabled': false})
        $('#sname').attr({'value': '', 'disabled': false})
        $('#city').attr({'value': '', 'disabled': false})
        $('#district').val('').attr('disabled', false);
        $('#state').val('').attr('disabled', false);
        $('#pincode').attr({'value': '', 'disabled': false})
    }
});
$("#id_state").change(function getdistricts() {
        const url = $("#contactform").attr("data-districts-url");
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

$("#id_state").change(function getdistricts() {
        const url = $("#contactform").attr("data-districts-url");
        const stateid = $(this).val();

        $.ajax({
            url: url,
            data: {
                'stateid': stateid
            },
            success: function (data) {
                $("#district").html(data);
            }
        });
    });

