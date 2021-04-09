function alphaOnly(event) {
  let key = event.keyCode;
  return ((key >= 65 && key <= 90) || key === 8);
    }
    function numOnly(event) {
    let key = event.keyCode;
  return ((key >= 48 && key <= 57) || (key >= 96 && key <= 105) || key === 8);
    }
$(document).ready(function(){
load_deps();
 });


    function load_deps(){
   const url = 'ajax/load_dependent';
        $.ajax({
            url: url,
            success: function (data) {
                $('#dep_list').html(data);

            }
        });
    }
   $("#add_dep").click(function(){
        $.ajax({
            url: 'ajax/add_dependent',
            type: 'get',
            dataType: 'json',
            // beforeSend: function () {
            // $(".add-popup").addClass('active');
            // },
            success: function (data) {
                $('#add_dependent').html(data.html_form);
                $(".add-popup").addClass('active');
            }
        });
    // document.querySelector(".add-popup").classList.add("active");
    });
    document.querySelector(".add-popup .close-btn").addEventListener("click",function(){
    document.querySelector(".add-popup").classList.remove("active");
    });
$("#add_dependent").on("submit", ".dep-add-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          alert("Book created!");  // <-- This is just a placeholder for now for testing
        }
        else {
          $("#add_dependent").html(data.html_form);
        }
      }
    });
    return false;
  });