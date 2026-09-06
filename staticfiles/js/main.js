/* =================================
   THEME SYSTEM
================================= */

const html = document.documentElement;

const themeToggle = document.getElementById("theme-toggle");
const themeIcon = document.getElementById("theme-icon");


/* =================================
   APPLY THEME
================================= */

function applyTheme(theme) {

    const isLight = theme === "light";

    html.classList.toggle("light", isLight);

    localStorage.setItem(
        "theme",
        isLight ? "light" : "dark"
    );

    updateThemeIcon(isLight);
    updateBackgroundImages(isLight);
}


/* =================================
   THEME ICON
================================= */

function updateThemeIcon(isLight) {

    if (!themeIcon) return;


    if (isLight) {

        /* Sun */

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

        themeToggle?.setAttribute(
            "aria-label",
            "Switch to dark theme"
        );

    } else {

        /* Moon */

        themeIcon.innerHTML = `
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M21.752 15.002A9.718 9.718 0 0118 15.75
                   A9.75 9.75 0 018.25 6c0-1.327.264-2.592.742-3.742
                   A9.753 9.753 0 1021.752 15.002z"
            />
        `;

        themeToggle?.setAttribute(
            "aria-label",
            "Switch to light theme"
        );
    }
}


/* =================================
   BACKGROUND IMAGE
================================= */

function updateBackgroundImages(isLight) {

    const backgroundImages =
        document.querySelectorAll(
            "[data-dark-src][data-light-src]"
        );


    backgroundImages.forEach((image) => {

        const darkSrc =
            image.dataset.darkSrc;

        const lightSrc =
            image.dataset.lightSrc;


        if (isLight) {

            if (image.src !== lightSrc) {
                image.src = lightSrc;
            }

        } else {

            if (image.src !== darkSrc) {
                image.src = darkSrc;
            }
        }
    });
}


/* =================================
   INITIAL THEME
================================= */

const savedTheme =
    localStorage.getItem("theme");


const initialTheme =
    savedTheme === "light"
        ? "light"
        : "dark";


applyTheme(initialTheme);


/* =================================
   THEME TOGGLE
================================= */

if (themeToggle) {

    themeToggle.addEventListener(
        "click",
        () => {

            const isCurrentlyLight =
                html.classList.contains("light");


            const newTheme =
                isCurrentlyLight
                    ? "dark"
                    : "light";


            applyTheme(newTheme);
        }
    );
}


/* =================================
   NAVBAR SCROLL
================================= */

document.addEventListener(
    "DOMContentLoaded",
    () => {

        const navbar =
            document.getElementById("main-navbar");


        if (!navbar) return;


        let lastScrollY =
            window.scrollY;


        function updateNavbar() {

            const currentScrollY =
                window.scrollY;


            /* -----------------------------
               Scrolled State
            ----------------------------- */

            if (currentScrollY > 20) {

                navbar.classList.add(
                    "navbar-scrolled"
                );

            } else {

                navbar.classList.remove(
                    "navbar-scrolled"
                );
            }


            /* -----------------------------
               Hide / Show Navbar
            ----------------------------- */

            if (
                currentScrollY > lastScrollY &&
                currentScrollY > 100
            ) {

                navbar.classList.add(
                    "navbar-hidden"
                );

            } else {

                navbar.classList.remove(
                    "navbar-hidden"
                );
            }


            lastScrollY =
                currentScrollY;
        }


        window.addEventListener(
            "scroll",
            updateNavbar,
            {
                passive: true
            }
        );


        updateNavbar();
    }
);


/* =================================
   CURSOR GLOW
================================= */

document.addEventListener(
    "DOMContentLoaded",
    () => {

        const cursorGlow =
            document.getElementById(
                "cursor-glow"
            );


        if (!cursorGlow) return;


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

                mouseX =
                    event.clientX;

                mouseY =
                    event.clientY;


                cursorGlow.classList.add(
                    "visible"
                );
            }
        );


        /* ---------------------------------
           Hide When Mouse Leaves
        --------------------------------- */

        document.addEventListener(
            "mouseleave",
            () => {

                cursorGlow.classList.remove(
                    "visible"
                );
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
    }
);
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

/* =================================
   CONTACT SUCCESS MODAL
================================= */

document.addEventListener("DOMContentLoaded", () => {

    const modal = document.getElementById(
        "contact-success-modal"
    );

    if (!modal) {
        return;
    }


    const closeButtons =
        modal.querySelectorAll(
            "[data-close-modal]"
        );


    const sendAgainButton =
        document.getElementById(
            "send-again-button"
        );


    /* =================================
       CLOSE MODAL
    ================================= */

    function closeModal() {

        modal.remove();

        document.body.style.overflow = "";

    }


    /* =================================
       PREVENT BACKGROUND SCROLL
    ================================= */

    document.body.style.overflow = "hidden";


    /* =================================
       CLOSE BUTTONS
    ================================= */

    closeButtons.forEach((button) => {

        button.addEventListener(
            "click",
            closeModal
        );

    });


    /* =================================
       SEND AGAIN
    ================================= */

    if (sendAgainButton) {

        sendAgainButton.addEventListener(
            "click",
            () => {

                closeModal();


                const form =
                    document.querySelector(
                        ".contact-form"
                    );


                if (!form) {
                    return;
                }


                form.scrollIntoView({
                    behavior: "smooth",
                    block: "center"
                });


                const firstInput =
                    form.querySelector(
                        "input:not([type='hidden']), textarea"
                    );


                if (firstInput) {

                    setTimeout(() => {

                        firstInput.focus();

                    }, 500);

                }

            }
        );

    }


    /* =================================
       ESCAPE KEY
    ================================= */

    document.addEventListener(
        "keydown",
        (event) => {

            if (
                event.key === "Escape" &&
                document.getElementById(
                    "contact-success-modal"
                )
            ) {

                closeModal();

            }

        }
    );

});