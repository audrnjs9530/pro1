function toggleUserMenu() {
    const menu = document.getElementById('userMenu');
    if (menu) {
        menu.classList.toggle('open');
    }
}

document.addEventListener('click', (event) => {
    const menu = document.getElementById('userMenu');
    if (menu && !menu.contains(event.target)) {
        menu.classList.remove('open');
    }
});
