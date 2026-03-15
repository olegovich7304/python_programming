$(document).ready(function(){
var yPosition;
var scrolled = 0;
var $parallaxElements = $('.icons-for-parallax img');
$(window).scroll(function() {
scrolled = $(window).scrollTop();
for (var i = 0; i < $parallaxElements.length; i++){
yPosition = (scrolled * 0.15*(i + 1));
$parallaxElements.eq(i).css({ top: yPosition });
}

window.addEventListener("scroll", function() {
    let scroll = window.pageYOffset;
    let logo = document.getElementById("logo");

    logo.style.transform = 
        "translate(-50%, calc(-50% + " + scroll * 0.3 + "px))";
});
});
});