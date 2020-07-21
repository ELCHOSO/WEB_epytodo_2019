function is_register_ok() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("pass").value;
    submitOK = "true";

    if (username.length < 4) {
        alert("Your username must be at least 4 characters long.");
        submitOK = "false";
    }

    if (password.length < 8) {
        alert("Your password must be at least 8 characters long.");
        submitOK = "false";
    }

    if (submitOK == "false") {
        return (false);
    }
    return (true);
}