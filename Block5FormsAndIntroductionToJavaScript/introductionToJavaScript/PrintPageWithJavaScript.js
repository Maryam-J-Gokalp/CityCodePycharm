<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Print Page Example</title>

    <script type="text/javascript">
        "use strict";

        // Function to get an element by ID (shortcut function)
        var $ = function(id) {
            return document.getElementById(id);
        };

        // Function to trigger the print dialog
        var printPage = function() {
            window.print();
        };

        // Assign the printPage function to the button click event when the page loads
        window.onload = function() {
            $("printButton").onclick = printPage;
        };
    </script>
</head>
<body>

    <h1>Click the button below to print the page</h1>

    <!-- Button to trigger the print function -->
    <input type="button" id="printButton" value="Print the Page">

</body>
</html>
