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
        // Start the table and add headers
        document.write("<table border='1'>");
        document.write("<tr><th>Key</th><th>Value</th></tr>"); // Table headers

        let fieldParts;
        fields.forEach(field => {
            fieldParts = field.split("=");
            fieldParts[0] = decodeURIComponent(fieldParts[0].replace(/\+/g, " "));
            fieldParts[1] = decodeURIComponent(fieldParts[1].replace(/\+/g, " "));

            // Add each key-value pair as a table row
            document.write("<tr>");
            document.write("<th>" + fieldParts[0] + "</th>");  // Column for key
            document.write("<td>" + fieldParts[1] + "</td>");   // Column for value
            document.write("</tr>");
        });

        document.write("</table>"); // End of the table
    }
};
