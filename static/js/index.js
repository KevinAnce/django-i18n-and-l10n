document.addEventListener("DOMContentLoaded", () => {
    const modalElement = document.getElementById("modal");
    const signupButton = document.getElementById("signup-button");
    const loginButton = document.getElementById("login-button");
    const modal = new bootstrap.Modal(modalElement);
    const modalHelpText = document.getElementById("modal-help-text");
    const modalButton = document.getElementById("modal-button");
    const modalTitle = document.getElementById("modal-title");

    signupButton.addEventListener("click", () => {
        modalTitle.innerHTML = gettext("Sign up for free");
        modalButton.innerHTML = gettext("Sign up");
        modalHelpText.innerHTML = gettext("By clicking Sign up, you agree to the terms of use.");
        modal.show();
    });

    loginButton.addEventListener("click", () => {
        modalTitle.innerHTML = gettext("Login now");
        modalButton.innerHTML = gettext("Log in");
        modalHelpText.innerHTML = "";
        modal.show();
    });
});