function alphaOnly(event) {
  let key = event.keyCode;
  return ((key >= 65 && key <= 90) || key === 8);
    }

    function numOnly(event) {
    let key = event.keyCode;
  return ((key >= 48 && key <= 57) || (key >= 96 && key <= 105) || key === 8);
    }

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