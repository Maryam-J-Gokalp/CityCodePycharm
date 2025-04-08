$("#member_form").submit(event => {
    let isValid = true;
    const emailPattern = /\b{A-Za-z0-9. %+-}+@{A-Za-z0-9.-}+\.{A-Za-z}{2,4}\b/;
    const  email= $("#email").val().trim();
})