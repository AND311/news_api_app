document.addEventListener("DOMContentLoaded", function () {
    const themeSelect = document.getElementById("themeSelect");
    const sourceSelect = document.getElementById("sourceSelect");
    const saveSettings = document.getElementById("saveSettings");

    // Carica il tema salvato
    let savedTheme = localStorage.getItem("theme") || "light";
    applyTheme(savedTheme);
    themeSelect.value = savedTheme;

    // Carica la fonte selezionata
    let savedSource = localStorage.getItem("source") || "";
    fetch("/dropdown")
        .then(response => response.json())
        .then(sources => {
            sourceSelect.innerHTML = '<option value="">Select a source</option>'; // Reset options
            sources.forEach(source => {
                let option = document.createElement("option");
                option.value = source.id;
                option.textContent = source.name;
                if (source.id === savedSource) {
                    option.selected = true;
                }
                sourceSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error("Error loading sources:", error);
            sourceSelect.innerHTML = '<option value="">Failed to load sources</option>';
        });

    // Salva le impostazioni quando l'utente preme "Save"
    saveSettings.addEventListener("click", function () {
        let selectedTheme = themeSelect.value;
        let selectedSource = sourceSelect.value;
        
        // Apply the selected theme
        applyTheme(selectedTheme);
        
        // Save the selected settings to localStorage
        localStorage.setItem("theme", selectedTheme);
        localStorage.setItem("source", selectedSource);

        // Redirect the user to the same URL with the source as a query parameter
        const currentURL = window.location.href.split('?')[0]; // Get the base URL without query params
        const newURL = `${currentURL}?query=latest&sources=${selectedSource}`; // Append the source query parameter
        window.location.href = newURL; // Redirect to the updated URL
    });

    // Apply the theme
    function applyTheme(theme) {
        if (theme === "dark") {
            document.documentElement.setAttribute("data-bs-theme", "dark");
            document.body.classList.add("bg-dark", "text-white");
        } else {
            document.documentElement.setAttribute("data-bs-theme", "light");
            document.body.classList.remove("bg-dark", "text-white");
        }
    }
});
