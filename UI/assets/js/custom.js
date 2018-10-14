

var loginForm = document.getElementById("login-form");
var wrongUsername = document.getElementById('wrong-username');
var wrongPasword = document.getElementById('wrong-pasword');

loginForm.addEventListener("submit", function (e) {
    e.preventDefault();
    var username = e.target.username.value;
    var password = e.target.password.value;

    if (username == '')
        wrongUsername.style.visibility = 'visible';

    if (password == '')
        wrongPasword.style.visibility = 'visible';

    if (username == 'admin' && password == 'admin')
        window.location.href = 'admin/dashboard.html';

    if (username == 'attendant' && password == 'attendant')
        window.location.href = 'attendant/dashboard.html';
    
});
