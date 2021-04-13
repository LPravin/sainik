$(document).on("submit", "#dep_update_form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
            $(".popup").removeClass('active');
            load_deps();
        }
        else {
          $("#dep_update_dependent").html(data.html_form);
        }
      }
    });
    return false;
  });
$(document).ready(function(){
load_deps();
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
            $(".add-popup").removeClass('active');
            load_deps();
        }
        else {
          $("#add_dependent").html(data.html_form);
        }
      }
    });
    return false;
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
       const url = 'ajax/add_dependent';
        $.ajax({
            url: url,
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
    });

$(document).on('click','.edit_dep', function (event){
        // alert('I AM CLICKED');
        const btn =$(this);
        $.ajax({
            url: btn.attr('data-url'),
            type: 'get',
            dataType: 'json',
            success: function (data){
                $('#update_dependent').html(data.html_form);
                $(".popup").addClass('active');
            }
        })
    });

$(document).on("click", ".delete", function () {
    var form = $(this);
    $.ajax({
      url: form.attr('data-url'),
      success: function (data) {
            $('#dep_list').html(data);
    }})
  });

function alphaOnly(event) {
  let key = event.keyCode;
  return ((key >= 65 && key <= 90) || key === 8);
    }
    function numOnly(event) {
    let key = event.keyCode;
  return ((key >= 48 && key <= 57) || (key >= 96 && key <= 105) || key === 8);
    }
