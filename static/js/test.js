// let timeout;

// function myFunction() {
//   timeout = setTimeout(myMain, 10000);
// }

// function myMain() {
//     document.getElementById("loads").style.display = "none";
//     document.getElementsByTagName("body").css("overflow", "hidden");
// }

// window.addEventListener('load', myFunction);
document.onreadystatechange = function() {
  if (document.readyState !== "complete") {
      document.querySelector(
        "body").style.visibility = "hidden";
      document.querySelector(
        "#loads").style.visibility = "visible";
  } else {
      document.querySelector(
        "#loads").style.display = "none";
      document.querySelector(
        "body").style.visibility = "visible";
  }
};

function myFunction() {
  var x = document.getElementById("myInput");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}