AOS.init();

window.onscroll = function() {scrollFunction()};
const changeDOM = document.getElementById('header');
function scrollFunction() {
  if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
    changeDOM.style.height = "154vh";
  } 
  else if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 400) {
    changeDOM.style.height = "153vh";
  } 
  else if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
    changeDOM.style.height = "152vh";
  } 
  else if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
    changeDOM.style.height = "148vh";
  } 
  else if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    changeDOM.style.height = "146vh";
  } 
  else if(document.body.scrollTop > 90 || document.documentElement.scrollTop > 90) {
    changeDOM.style.height = "144vh";
  }
  else if(document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
    changeDOM.style.height = "142vh";
  }
  else if(document.body.scrollTop > 10 || document.documentElement.scrollTop > 10) {
    changeDOM.style.height = "141vh";
  }
}

