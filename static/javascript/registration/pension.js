// $(document).ready(function (){
//         const url = $("#pensionform").attr("data-mcs-url");
//
//         $.ajax({
//             url: url,
//             data: {
//                 'service_id': serviceid,
//                  'groupid' :  groupid
//             },
//             success: function (data) {
//                 $("#id_trade").html(data);
//
//             }
//         });
//     });

function details(evt, tabName) {

  var i;
  var x = document.getElementsByClassName("tab");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  document.getElementById(tabName).style.display = "block";
}

     document.getElementById("defaultOpen").click();

function alphaOnly(event) {
  let key = event.keyCode;
  return ((key >= 65 && key <= 90) || key === 8);
    }

    function numOnly(event) {
    let key = event.keyCode;
  return ((key >= 48 && key <= 57) || (key >= 96 && key <= 105) || key === 8);
    }