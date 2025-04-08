const display_data = () => {
    const urlParts = window.location.toString().split("?");

    // Check if there are query parameters
    if (urlParts.length !== 2) {
        document.write("<p>No data was submitted.</p>");
        return;
    }

    const fields = urlParts[1].split("&");

    if (fields.length === 0) {
        document.write("<p>No data was submitted.</p>");
    } else {
        document.write("<table>");
        let fieldParts;
        fields.forEach(field => {
            fieldParts = field.split("=");
            fieldParts[0] = decodeURIComponent(fieldParts[0].replace(/\+/g, " "));
            fieldParts[1] = decodeURIComponent(fieldParts[1].replace(/\+/g, " "));

            // Display each field in a table row
            document.write("<tr>");
            document.write("<td>" + fieldParts[0] + "</td>");
            document.write("<td>" + fieldParts[1] + "</td>");
            document.write("</tr>");
        });
        document.write("</table>");
    }
};
