function filtrarEmpleados() {
    const input = document.getElementById("busqueda");
    const filtro = input.value.toLowerCase();
    const tabla = document.getElementById("tablaEmpleados");
    const filas = tabla.getElementsByTagName("tr");

    for (let i = 1; i < filas.length; i++) {
        const celdas = filas[i].getElementsByTagName("td");
        let coincide = false;

        for (let j = 0; j < celdas.length; j++) {
            if (celdas[j]) {
                const texto = celdas[j].textContent || celdas[j].innerText;
                if (texto.toLowerCase().indexOf(filtro) > -1) {
                    coincide = true;
                    break;
                }
            }
        }
        filas[i].style.display = coincide ? "" : "none";
    }
}

const notificacionSwal = (titleText, text, icon, confirmButtonText) => {
    return Swal.fire({
        title: titleText,
        text: text,
        icon: icon,
        confirmButtonText: confirmButtonText,
    });
};

document.addEventListener("DOMContentLoaded", function () {
    const guardarButtons = document.querySelectorAll('.·n-guardar');

    guardarButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            const form = this.closest('form');

            Swal.fire({
                title: "¿Confirma el cambio de contraseña?",
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Cambiar",
                cancelButtonText: "Cancelar",
                confirmButtonColor: "#d33",
                cancelButtonColor: "#3085d6",
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm: () => form.submit(),
                allowOutsideClick: false,
                allowEscapeKey: false,
            });
        });
    });

    document.addEventListener('click', function (event) {
        if (event.target.classList.contains('btn-borrar')) {
            event.preventDefault();
            const form = event.target.closest('form');

            Swal.fire({
                title: "¿Confirma la eliminación del usuario?",
                text: "Esta acción no se puede deshacer.",
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Eliminar",
                cancelButtonText: "Cancelar",
                confirmButtonColor: "#d33",
                cancelButtonColor: "#3085d6",
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm: () => form.submit(),
                allowOutsideClick: false,
                allowEscapeKey: false,
            });
        }
    });

    const showAlertForMessages = () => {
        const successMessage = document.querySelector('.alert-success');
        const errorMessage = document.querySelector('.alert-danger');

        if (successMessage) {
            notificacionSwal('¡Éxito!', successMessage.textContent, 'success', 'Aceptar');
        } else if (errorMessage) {
            notificacionSwal('Error', errorMessage.textContent, 'error', 'Intentar de nuevo');
        }
    };

    showAlertForMessages();
});

function modal_editar(url) {
    const $ = jQuery.noConflict();
    $('#edicion').load(url, function () {
        $(this).modal('show');
    });
}

function modal_agregar(url) {
    const $ = jQuery.noConflict();
    $('#agregar').load(url, function () {
        $(this).modal('show');
    });
}

function modal_clave(url) {
    const $ = jQuery.noConflict();
    $('#clave').load(url, function () {
        $(this).modal('show');
        showAlertForMessages();
    });
}
