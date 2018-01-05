const loginButton = document.getElementById('id_login_button');
loginButton.addEventListener('click', (event) => {
  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/users/login/');
  xhr.onreadystatechange = function () {
    if (xhr.status === 400) {
      alert(xhr.responseText);
    }
  };
  xhr.send();
});
