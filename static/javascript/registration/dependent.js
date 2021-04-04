function alphaOnly(event) {
  let key = event.keyCode;
  return ((key >= 65 && key <= 90) || key === 8);
    }
    function numOnly(event) {
    let key = event.keyCode;
  return ((key >= 48 && key <= 57) || (key >= 96 && key <= 105) || key === 8);
    }
    var a = document.getElementById("id_form-TOTAL_FORMS");
    $("#addform").click(function (){
      $(".user-details:hidden:first").attr("hidden", false);
      if(a.value < 5) {
        a.value = parseInt(a.value) + 1;
      }
    });
    $("#removeform").click(function (){
      $(".user-details:visible:last").attr("hidden", true);
      var b = a.value - 1;
      $(".form-"+b).val("");
      if(a.value > 0) {
        a.value = parseInt(a.value) - 1;
      }
    });

    // $(document).ready(function(){
    //   form0_input = document.getElementsByClassName(".form-0");
    //   form1_input = document.getElementsByClassName(".form-1");
    //   form2_input = document.getElementsByClassName(".form-2");
    //   form3_input = document.getElementsByClassName(".form-3");
    //   form4_input = document.getElementsByClassName(".form-4");
    // });