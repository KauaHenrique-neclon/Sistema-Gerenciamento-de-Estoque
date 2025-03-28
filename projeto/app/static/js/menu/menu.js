document.addEventListener('DOMContentLoaded', function() {
    const subMenus = document.querySelectorAll('.li-subMenu > a');

    subMenus.forEach(menu => {
        menu.addEventListener('click', function(e) {
            e.preventDefault();

            const subMenuList = this.nextElementSibling;

            if (subMenuList) {
                subMenuList.classList.toggle('show');
            }
        });
    });
});


document.querySelectorAll('.menu-toggle').forEach(item => {
    item.addEventListener('click', function(e) {
        e.preventDefault(); // Evita que a página pule
        const submenu = this.nextElementSibling; // Seleciona o submenu correspondente

        if (submenu) {
            submenu.classList.toggle('show'); // Alterna a classe 'show'
        }

        // Fecha outros submenus
        document.querySelectorAll('.li-subMenu').forEach(otherSubmenu => {
            if (otherSubmenu !== submenu) {
                otherSubmenu.classList.remove('show');
            }
        });
    });
});