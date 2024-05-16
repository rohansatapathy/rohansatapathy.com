function setCookie(name, value) {
    document.cookie = name + "=" + value + "; path=/"
}

function getCookie(cookieName) {
    let name = cookieName + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(";");
    for (let i = 0; i < ca.length; i++) {
        let cookie = ca[i];
        while (cookie.charAt(0) == ' ') {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(name) == 0) {
            return cookie.substring(name.length, cookie.length);
        }
    }
    return "";
}

function getTheme() {
    return getCookie("theme");
}

function getSystemTheme() {
    const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)')
    return prefersDarkMode.matches ? 'dark' : 'light'
}

// theme must be either "light", "dark", or "auto"
function setTheme(theme, button) {
    var newTheme = theme;
    if (theme == "auto") {
        newTheme = getSystemTheme();
    }
    document.documentElement.setAttribute('data-bs-theme', newTheme);
    document.documentElement.setAttribute('data-theme', theme);  // For icon switching
    setCookie("theme", theme);
    // button.innerHTML = theme;
}

const themeButton = document.getElementById("theme-button")
themeButton.addEventListener("click", () => {
    let currentTheme = getTheme();
    var newTheme;
    if (currentTheme == "auto") {
        newTheme = "light";
    } else if (currentTheme == "light") {
        newTheme = "dark";
    } else {
        newTheme = "auto";
    }
    setTheme(newTheme, themeButton);
});

let theme = getTheme()
if (theme != "") {
    setTheme(theme, themeButton);
} else {
    setTheme("auto", themeButton);
}

// Automatically change if preference changes and current mode is auto
const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)');
prefersDarkMode.addEventListener("change", () => {
    if (getTheme() == "auto") {
        setTheme("auto", themeButton);
    }
})

