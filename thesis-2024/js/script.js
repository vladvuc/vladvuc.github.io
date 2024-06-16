//Get the button
var mybutton = document.getElementById("toTop");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

function checkHash() {
  console.log("Hash started");
  if (window.location.hash === "#project-management") {
    const button = document.querySelector("#project-management button");
    if (button) {
      button.click();
      window.scrollBy(0, -90);
    }
  } else if (window.location.hash === "#software-engineering") {
    const button = document.querySelector("#software-engineering button");
    if (button) {
      button.click();
      button.scrollIntoView({
        block: "start",
        inline: "nearest",
        behavior: "smooth",
      });
      window.scrollBy(0, -90);
    }
  }
}

window.addEventListener("hashchange", checkHash, false);
window.addEventListener("DOMContentLoaded", checkHash, false);
