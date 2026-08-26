/* =========================================
   PROJECT DATA
========================================= */

const projectData = {

    fryx: {
        title: "Fryx",

        image: "/static/images/hero-bg.png",

        description:
            "Fryx is an AI-powered assistant platform designed " +
            "for intelligent conversations, contextual search, " +
            "and modern productivity workflows.",

        features: [
            "AI-powered conversational interface",
            "Context-aware search and responses",
            "Modern responsive interface",
            "Backend API architecture",
            "Persistent project data"
        ],

        technologies: [
            "Python",
            "Django",
            "PostgreSQL",
            "JavaScript"
        ],

        github: "https://github.com/",
        live: "#"
    },


    threadly: {
        title: "Threadly",

        image: "/static/images/hero-bg.png",

        description:
            "Threadly is a full-stack discussion platform focused " +
            "on structured communities, authentication, content " +
            "management, and scalable APIs.",

        features: [
            "User authentication",
            "Community-based discussions",
            "REST API architecture",
            "Content management",
            "PostgreSQL database integration"
        ],

        technologies: [
            "Python",
            "Django",
            "PostgreSQL",
            "REST API"
        ],

        github: "https://github.com/",
        live: "#"
    }

};


/* =========================================
   MODAL ELEMENTS
========================================= */

const projectModal =
    document.getElementById("project-modal");

const projectModalClose =
    document.getElementById("project-modal-close");

const projectModalBackdrop =
    document.querySelector(".project-modal-backdrop");

const modalTitle =
    document.getElementById("modal-project-title");

const modalImage =
    document.getElementById("modal-project-image");

const modalDescription =
    document.getElementById("modal-project-description");

const modalFeatures =
    document.getElementById("modal-project-features");

const modalTechnologies =
    document.getElementById("modal-project-technologies");

const modalLinks =
    document.getElementById("modal-project-links");


/* =========================================
   OPEN MODAL
========================================= */

function openProjectModal(projectId) {

    const project = projectData[projectId];

    if (!project) {
        return;
    }


    /* Title */

    modalTitle.textContent = project.title;


    /* Image */

    modalImage.src = project.image;

    modalImage.alt =
        `${project.title} project preview`;


    /* Description */

    modalDescription.textContent =
        project.description;


    /* Features */

    modalFeatures.innerHTML = "";

    project.features.forEach((feature) => {

        const item =
            document.createElement("li");

        item.textContent = feature;

        modalFeatures.appendChild(item);

    });


    /* Technologies */

    modalTechnologies.innerHTML = "";

    project.technologies.forEach((technology) => {

        const tag =
            document.createElement("span");

        tag.textContent = technology;

        modalTechnologies.appendChild(tag);

    });


    /* Links */

    modalLinks.innerHTML = "";


    if (project.github) {

        const github =
            document.createElement("a");

        github.href = project.github;

        github.target = "_blank";

        github.rel = "noopener noreferrer";

        github.textContent = "GitHub ↗";

        modalLinks.appendChild(github);

    }


    if (project.live && project.live !== "#") {

        const live =
            document.createElement("a");

        live.href = project.live;

        live.target = "_blank";

        live.rel = "noopener noreferrer";

        live.textContent = "Live Demo ↗";

        modalLinks.appendChild(live);

    }


    /* Show modal */

    projectModal.classList.add("is-open");

    projectModal.setAttribute(
        "aria-hidden",
        "false"
    );


    /* Prevent background scrolling */

    document.body.style.overflow = "hidden";

}


/* =========================================
   CLOSE MODAL
========================================= */

function closeProjectModal() {

    projectModal.classList.remove("is-open");

    projectModal.setAttribute(
        "aria-hidden",
        "true"
    );


    document.body.style.overflow = "";

}


/* =========================================
   SHOW DETAILS BUTTONS
========================================= */

document
    .querySelectorAll("[data-project-open]")
    .forEach((button) => {

        button.addEventListener("click", () => {

            const projectId =
                button.dataset.projectOpen;

            openProjectModal(projectId);

        });

    });


/* =========================================
   CLOSE BUTTON
========================================= */

if (projectModalClose) {

    projectModalClose.addEventListener(
        "click",
        closeProjectModal
    );

}


/* =========================================
   BACKDROP CLICK
========================================= */

if (projectModalBackdrop) {

    projectModalBackdrop.addEventListener(
        "click",
        closeProjectModal
    );

}


/* =========================================
   ESCAPE KEY
========================================= */

document.addEventListener(
    "keydown",
    (event) => {

        if (
            event.key === "Escape" &&
            projectModal.classList.contains("is-open")
        ) {

            closeProjectModal();

        }

    }
);