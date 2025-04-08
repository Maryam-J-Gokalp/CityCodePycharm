const display_data = () => {
    const urlParts = window.location.toString().split("?");

    if (urlParts.length !== 2) return;

    const fields = urlParts[1].split("&");

    fields.forEach(field => {
        const [key, value] = field.split("=");
        if (key && value) {
            const decodedValue = decodeURIComponent(value.replace(/\+/g, " "));
            const element = document.getElementById(key);
            if (element) {
                element.textContent = decodedValue;
            }
        }
    });
};
