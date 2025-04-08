const decode = (text) => {
    // Replace '+' with space
    text = text.replace(/\+/g, " ");

    // Replace %XX with corresponding character
    text = text.replace(/%[a-fA-F0-9]{2}/g, (match) => {
        return String.fromCharCode(parseInt(match.substr(1, 2), 16));
    });

    return text;
};

// Example usage:
const encodedText = "Hello%20World%21+Test";
console.log(decode(encodedText));  // Output: Hello World! Test
