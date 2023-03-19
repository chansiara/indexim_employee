$(document).ready(function(){
  var loadForm = function() {
    var btn = $(this);
    $.ajax({
      url: btn.attr("href"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal").modal("show");
      },
      success: function (data) {
        $("#modal .modal-content").html(data.html_form);
      }
    });
    return false;
  };

  var saveForm = function() {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      beforeSend: function () {
        $(".loading-icon").removeClass("hide");
        $(".btn").attr("disabled", true);
        $(".btn-txt").text("Loading....");
      },
      success: function (data) {
        if (data.form_is_valid) {
          $(".btn").attr("disabled", false);          
          $(".table tbody").html(data.list);
          $("#modal").modal("hide");
          var val = "Simpan";
          if (this.url.indexOf("delete") >= 0) {
            val = "Hapus"
          }
          Swal.fire({
            "title":"Aksi Berhasil",
            "text":"Berhasil "+ val + " Data...",
            "icon":"success"
          });
        }
        else {
          $("#modal .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  var saveFormDelPO = function() {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      beforeSend: function () {
        $(".loading-icon").removeClass("hide");
        $(".btn").attr("disabled", true);
        $(".btn-txt").text("Loading....");
      },
      success: function (data) {
        if (data.form_is_valid) {
          $(".btn").attr("disabled", false);          
          $(".table tbody").html(data.list);
          $("#modal").modal("hide");
          var val = "Simpan";
          if (this.url.indexOf("delete") >= 0) {
            val = "Hapus"
          }
          Swal.fire({
            "title":"Aksi Berhasil",
            "text":"Berhasil "+ val + " Data...",
            "icon":"success"
          });
        }
        else {
          $(".btn").attr("disabled", false);  
          $("#modal").modal("hide");
          Swal.fire({
            "title":"PO Tidak Dihapus",
            "text":"PO yang sudah diproses Receive tidak dapat dihapus!",
            "icon":"error"
          });
        }
      }
    });
    return false;
  };

    var saveFormwImage = function() {
    var form = $(this);
    var fd = new FormData(this);
    $.ajax({
      url: form.attr("action"),
      data: fd,
      type: form.attr("method"),
      dataType: 'json',
      processData: false,
      contentType: false,
      success: function (data) {
        if (data.form_is_valid) {
          $("#table tbody").html(data.list);
          $("#modal").modal("hide");
          var val = "Simpan";
          if (this.url.indexOf("delete") >= 0) {
            val = "Hapus"
          }
          Swal.fire({
        "title":"Aksi Berhasil",
        "text":"Berhasil "+ val + " Data...",
        "icon":"success"
      });
        }
        else {
          $("#modal .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  $("body").on('click', '.js-load-form', loadForm);
  $("body").on('submit', '.js-save-form', saveForm);
  $("body").on('submit', '.js-save-form-delpo', saveFormDelPO);
  $("body").on('submit', '.js-save-form-image', saveFormwImage);
});