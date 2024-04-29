const toggle = document.getElementById('toggle');

toggle.addEventListener('change', function() {
    document.body.classList.toggle('night-mode');
});