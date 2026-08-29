/* =================================
   THEME TOGGLE
================================= */

const themeToggle = document.getElementById("theme-toggle");
const themeIcon = document.getElementById("theme-icon");

if (themeToggle) {
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "light") {
        document.documentElement.classList.add("light");
    }

    themeToggle.addEventListener("click", () => {
        const isLight =
            document.documentElement.classList.toggle("light");

        localStorage.setItem(
            "theme",
            isLight ? "light" : "dark"
        );

        updateThemeIcon(isLight);
    });

    updateThemeIcon(
        document.documentElement.classList.contains("light")
    );
}


function updateThemeIcon(isLight) {

    if (!themeIcon) return;

    if (isLight) {

        themeIcon.innerHTML = `
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 3v2.25
                   M12 18.75V21
                   M4.22 4.22l1.59 1.59
                   M18.19 18.19l1.59 1.59
                   M3 12h2.25
                   M18.75 12H21
                   M4.22 19.78l1.59-1.59
                   M18.19 5.81l1.59-1.59
                   M16.5 12a4.5 4.5 0 11-9 0
                   4.5 4.5 0 019 0z"
            />
        `;

    } else {

        themeIcon.innerHTML = `
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M21.752 15.002A9.718 9.718 0 0118 15.75
                   A9.75 9.75 0 018.25 6c0-1.327.264-2.592.742-3.742
                   A9.753 9.753 0 1021.752 15.002z"
            />
        `;
    }
}


/* =================================
   NAVBAR SCROLL
================================= */

document.addEventListener("DOMContentLoaded", () => {

    const navbar = document.getElementById("main-navbar");

    if (!navbar) return;


    let lastScrollY = window.scrollY;


    function updateNavbar() {

        const currentScrollY = window.scrollY;


        /* -----------------------------
           Scrolled State
        ----------------------------- */

        if (currentScrollY > 20) {

            navbar.classList.add("navbar-scrolled");

        } else {

            navbar.classList.remove("navbar-scrolled");

        }


        /* -----------------------------
           Hide / Show Navbar
        ----------------------------- */

        if (
            currentScrollY > lastScrollY &&
            currentScrollY > 100
        ) {

            navbar.classList.add("navbar-hidden");

        } else {

            navbar.classList.remove("navbar-hidden");

        }


        lastScrollY = currentScrollY;
    }


    window.addEventListener(
        "scroll",
        updateNavbar,
        { passive: true }
    );


    updateNavbar();

});


/* =================================
   CURSOR RED GLOW
================================= */

document.addEventListener("DOMContentLoaded", () => {

    const cursorGlow =
        document.getElementById("cursor-glow");


    if (!cursorGlow) {
        console.warn("Cursor glow element not found.");
        return;
    }


    let mouseX = -300;
    let mouseY = -300;

    let glowX = mouseX;
    let glowY = mouseY;


    /* ---------------------------------
       Mouse Movement
    --------------------------------- */

    document.addEventListener(
        "mousemove",
        (event) => {

            mouseX = event.clientX;
            mouseY = event.clientY;

            cursorGlow.classList.add("visible");
        }
    );


    /* ---------------------------------
       Hide Glow When Mouse Leaves
    --------------------------------- */

    document.addEventListener(
        "mouseleave",
        () => {

            cursorGlow.classList.remove("visible");
        }
    );


    /* ---------------------------------
       Smooth Glow Animation
    --------------------------------- */

    function animateGlow() {

        glowX +=
            (mouseX - glowX) * 0.12;

        glowY +=
            (mouseY - glowY) * 0.12;


        cursorGlow.style.left =
            `${glowX}px`;

        cursorGlow.style.top =
            `${glowY}px`;


        requestAnimationFrame(
            animateGlow
        );
    }


    animateGlow();

});