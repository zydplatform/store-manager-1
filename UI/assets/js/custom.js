

var loginForm = document.getElementById("login-form");

loginForm.addEventListener("submit", function(e) {
    e.preventDefault();
    var username = e.target.username.value;
    var password = e.target.password.value;
    if (username == 'admin' && password == 'admin')
        window.location.href = 'admin/dashboard.html';
    else if (username == 'attendant' && password == 'attendant')
        window.location.href = 'attendant/dashboard.html';
        
});
