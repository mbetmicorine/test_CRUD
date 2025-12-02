document.addEventListener("DOMContentLoaded", () => {
    const container = document.querySelector(".icon-container");
    const buttons = {
        signup: document.getElementById("signup"),
        login: document.getElementById("login")
    };

    // Tableau des icônes possibles (emoji ou images)
    const icons = [
        "📄", // fichier
        "📁", // dossier
        "📚", // cahier
        "✏️", // crayon
        "🖊️", // stylo
        "🧽", // gomme
        "💻", // PC
        "📱", // téléphone
        "📝", // note
        "📒"  // carnet
    ];

    // Fonction pour créer un nouvel icône
    function createIcon() {
        const icon = document.createElement("div");
        icon.classList.add("file-icon");

        // Choisir aléatoirement un icône dans le tableau
        icon.textContent = icons[Math.floor(Math.random() * icons.length)];

        // Position de départ (gauche ou droite)
        icon.style.left = Math.random() < 0.5 ? "0px" : (window.innerWidth - 40) + "px";
        icon.style.bottom = "-40px";
        container.appendChild(icon);

        // Choisir un bouton cible aléatoire
        const target = Math.random() < 0.5 ? buttons.signup : buttons.login;
        moveIcon(icon, target);
    }

    function moveIcon(icon, target) {
        const targetRect = target.getBoundingClientRect();
        const iconRect = icon.getBoundingClientRect();
        const deltaX = targetRect.left + targetRect.width / 2 - (iconRect.left + iconRect.width / 2);
        const deltaY = targetRect.top + targetRect.height / 2 - (iconRect.top + iconRect.height / 2);

        // Animation
        icon.style.transition = "transform 2s ease-in-out, opacity 2s";
        icon.style.transform = `translate(${deltaX}px, ${deltaY}px) scale(0.5) rotate(360deg)`;
        icon.style.opacity = 1;

        // Disparaître avant suppression
        setTimeout(() => {
            icon.style.opacity = 0;
        }, 1800);

        setTimeout(() => {
            icon.remove();
        }, 2000);
    }

    // Générer automatiquement une icône toutes les 0.5 secondes
    setInterval(createIcon, 500);
});
