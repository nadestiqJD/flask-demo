// skrypt na ustawienie footera na dole strony
const header = document.getElementsByTagName("header")[0];
const navbar = document.getElementsByTagName("nav")[0];
const mainElement = document.getElementsByTagName("main")[0];
const footer = document.getElementsByTagName("footer")[0];
function resizeMain() {
    headerHeight = parseInt(getComputedStyle(header).height)
        + parseInt(getComputedStyle(header).marginTop) + parseInt(getComputedStyle(header).marginBottom);

    navbarHeight = parseInt(getComputedStyle(navbar).height)
        + parseInt(getComputedStyle(navbar).marginTop) + parseInt(getComputedStyle(navbar).marginBottom);

    footerHeight = parseInt(getComputedStyle(footer).height)
        + parseInt(getComputedStyle(footer).marginTop) + parseInt(getComputedStyle(footer).marginBottom);

    mainMarginHeight = parseInt(getComputedStyle(mainElement).marginTop) + parseInt(getComputedStyle(mainElement).marginBottom);

    var height = window.innerHeight- headerHeight - navbarHeight - mainMarginHeight - footerHeight;

    mainElement.style.minHeight = `${height}px`;
}
resizeMain();
addEventListener("resize", resizeMain);