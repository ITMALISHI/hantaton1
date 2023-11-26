function validateFormForRegister()
{
    let nameRegister = document.getElementById("nameRegister");
    let firstnameRegister = document.getElementById("firstnameRegister");
    let patronymicRegister = document.getElementById("patronymicRegister");
    let ageRegister = document.getElementById("ageRegister");
    let emaiRegister = document.getElementById("emaiRegister");
    let telNumberRegister = document.getElementById("telNumberRegister");
    let loginRegister = document.getElementById("loginRegister");
    let passwordRegister = document.getElementById("passwordRegister");
    let isValid = true;
    let errorMessages = document.querySelectorAll(".error-message");
    errorMessages.forEach(function (errorMessage)
    {
        errorMessage.remove();
    });
    nameRegister.style.borderColor = "";
    firstnameRegister.style.borderColor = "";
    patronymicRegister.style.borderColor = "";
    ageRegister.style.borderColor = "";
    emaiRegister.style.borderColor = "";
    telNumberRegister.style.borderColor = "";
    loginRegister.style.borderColor = "";
    passwordRegister.style.borderColor = "";
    if (nameRegister.value === "")
    {
        nameRegister.style.borderColor = "red";
        nameRegister.insertAdjacentHTML("afterend", "<p class='error-message' style='margin: 0'>Поле не заполнено</p>");
        isValid = false;
    }
    if (firstnameRegister.value === "")
    {
        firstnameRegister.style.borderColor = "red";
        firstnameRegister.insertAdjacentHTML("afterend", "<p class='error-message' style='margin: 0'>Поле не заполнено</p>");
        isValid = false;
    }
    if (patronymicRegister.value === "")
    {
        patronymicRegister.style.borderColor = "red";
        patronymicRegister.insertAdjacentHTML("afterend", "<p class='error-message' style='margin: 0'>Поле не заполнено</p>");
        isValid = false;
    }
    if (ageRegister.value === "")
    {
        ageRegister.style.borderColor = "red";
        ageRegister.insertAdjacentHTML("afterend", "<p class='error-message' style='margin: 0'>Поле не заполнено</p>");
        isValid = false;
    }
    if (emaiRegister.value === "")
    {
        emaiRegister.style.borderColor = "red";
        emaiRegister.insertAdjacentHTML("afterend", "<p class='error-message' style='margin: 0'>Поле не заполнено</p>");
        isValid = false;
    }
    if (telNumberRegister.value === "")
    {
        telNumberRegister.style.borderColor = "red";
        telNumberRegister.insertAdjacentHTML("afterend", "<p class='error-message' style='margin: 0'>Поле не заполнено</p>");
        isValid = false;
    }
    if (loginRegister.value === "")
    {
        loginRegister.style.borderColor = "red";
        loginRegister.insertAdjacentHTML("afterend", "<p class='error-message' style='margin: 0'>Поле не заполнено</p>");
        isValid = false;
    }
    if (passwordRegister.value === "")
    {
        passwordRegister.style.borderColor = "red";
        passwordRegister.insertAdjacentHTML("afterend", "<p class='error-message' style='margin: 0'>Поле не заполнено</p>");
        isValid = false;
    }
    return isValid;
}