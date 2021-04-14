

     $("#id_birth_state").change(function getdistricts() {
        const url = $("#personalform").attr("data-districts-url");
        const stateid = $(this).val();

        $.ajax({
            url: url,
            data: {
                'stateid': stateid
            },
            success: function (data) {
                $("#id_birth_district").html(data);
            }
        });
    });