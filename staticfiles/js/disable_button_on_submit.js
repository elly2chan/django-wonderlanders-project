const form = document.getElementById('form');
const submitButton = document.getElementById('submit');
form.addEventListener('submit', function () {
    submitButton.setAttribute('disabled', 'disabled');
    submitButton.value = 'Please wait...';
}, false);
