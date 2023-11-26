function validateFormForEnter()
{
    var login = document.getElementById("login");
    var Password = document.getElementById("Password");
    var isValid = true;
    var errorMessages = document.querySelectorAll(".error-message");
    errorMessages.forEach(function (errorMessage)
    {
        errorMessage.remove();
    });
    login.style.borderColor = "";
    Password.style.borderColor = "";

    if (login.value === "")
    {
        login.style.borderColor = "red";
        login.insertAdjacentHTML("afterend", "<p class='error-message' style='margin: 0'>Поле не заполнено</p>");
        isValid = false;
    }

    if (Password.value === "")
    {
        Password.style.borderColor = "red";
        Password.insertAdjacentHTML("afterend", "<p class='error-message' style='margin: 0'>Поле не заполнено</p>");
        isValid = false;
    }
    return isValid;
}