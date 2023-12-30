
// cart plus
$(".plus-cart").click(function () {
  var id = $(this).attr("pid").toString();
  var eml = this.parentNode.children[1];
  // console.log(id);
  $.ajax({
    type: "GET",
    url: "/pluscart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      eml.innerText = data.quantity;
      document.getElementById("ammount").innerText = data.ammount;
      document.getElementById("total_ammount").innerText = data.total_ammount;
    },
  });
});

//cart minus
$(".minus-cart").click(function () {
  var id = $(this).attr("pid").toString();
  var eml = this.parentNode.children[1];
  // console.log(id);
  $.ajax({
    type: "GET",
    url: "/minuscart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      eml.innerText = data.quantity;
      document.getElementById("ammount").innerText = data.ammount;
      document.getElementById("total_ammount").innerText = data.total_ammount;
    },
  });
});

//Remove cart product
$(".remove-cart").click(function () {
  var id = $(this).attr("pid").toString();
  var eml = this;
  // console.log(id);
  $.ajax({
    type: "GET",
    url: "/removecart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      document.getElementById("ammount").innerText = data.ammount;
      document.getElementById("total_ammount").innerText = data.total_ammount;
      eml.parentNode.parentNode.remove();
      // if (data.amount === 0) {
      // window.location.href = '/cart';
      // };
    },
  });
});
