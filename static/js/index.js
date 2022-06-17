
let timeout;

function myFunction() {
  timeout = setTimeout(myMain, 1500);
}

function myMain() {
    document.getElementById("loads").style.display = "none";
}
  

window.addEventListener('load', myFunction);

const new1 = document.getElementById("new1");
const old = document.getElementById("old");
function myFun(){
  new1.style.display = "flex";
}

// $(":button").click(function(e) {
//   $(".old").replaceWith($(".new"));
// });

// });
