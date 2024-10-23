document.addEventListener("DOMContentLoaded", function() {
    const cerrarSesionBtn = document.querySelector('#cerrar-sesion-btn');
    const cerrarCajaBtn = document.querySelector('#btn-cerrar');
    const urlLogin = "/login/"; // URL del login para redirección

    if (cerrarSesionBtn) {
        cerrarSesionBtn.addEventListener('click', function(event) {
            event.preventDefault();
            document.getElementById('logout-form').submit();
        });
    }

    if (cerrarCajaBtn) {
        cerrarCajaBtn.addEventListener('click', function(event) {
            event.preventDefault();
            Swal.fire({
                title: "¿Confirma cerrar la sesión en este momento?",
                text: "Tiene una caja abierta, la cual se cerrará con la sesión.",
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Ok",
                cancelButtonText: "Cancelar",
                confirmButtonColor: "#d33",
                cancelButtonColor: "#3085d6",
                showLoaderOnConfirm: true,
                preConfirm: () => {
                    return fetch('/cierre/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCsrfToken(),
                        },
                        body: JSON.stringify({ action: 'cerrar_caja' })
                    }).then(response => {
                        if (!response.ok) {
                            throw new Error('Error al cerrar la caja');
                        }
                        return Swal.fire({
                            title: "Caja cerrada con éxito",
                            icon: "success",
                        });
                    }).then(() => {
                        return Swal.fire({
                            title: "¿Desea cerrar sesión?",
                            icon: "question",
                            showCancelButton: true,
                            confirmButtonText: "Sí",
                            cancelButtonText: "No",
                        });
                    }).then(result => {
                        if (result.isConfirmed) {
                            document.getElementById('logout-form').submit();
                        } else {
                            window.location.href = '/menu/';
                        }
                    });
                },
                allowOutsideClick: false,
                allowEscapeKey: false,
            });
        });
    }

    document.querySelectorAll('#btn-cambiar').forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const form = this.closest('form');
            const password = form.querySelector('input[name="password"]').value;
            const passwordConfirm = form.querySelector('input[name="password_confirm"]').value;

            if (password !== passwordConfirm) {
                notificacionSwal("Error", "Las contraseñas no coinciden.", "error", "Ok");
                return;
            }

            Swal.fire({
                title: "¿Confirma cambiar la contraseña?",
                text: "Se pedirá que inicie sesión nuevamente con su nueva contraseña.",
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Ok",
                cancelButtonText: "Cancelar",
                confirmButtonColor: "#d33",
                cancelButtonColor: "#3085d6",
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm: () => form.submit(),
                allowOutsideClick: false,
                allowEscapeKey: false,
            }).then(result => {
                if (result.isConfirmed) {
                    notificacionSwal("Contraseña modificada con éxito", "", "success", "Ok").then(() => {
                        window.location.href = urlLogin;
                    });
                }
            });
        });
    });

    function getCsrfToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
    }

    const notificacionSwal = (titleText, text, icon, confirmButtonText) => {
        return Swal.fire({
            titleText: titleText,
            text: text,
            icon: icon,
            confirmButtonText: confirmButtonText,
        });
    };
});
