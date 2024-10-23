document.addEventListener("DOMContentLoaded", function() {
    const cerrarSesionBtn = document.querySelector('#cerrar-sesion-btn');
    const cerrarCajaBtn = document.querySelector('#btn-cerrar');

    if (cerrarSesionBtn) {
        cerrarSesionBtn.addEventListener('click', function(event) {
            event.preventDefault(); 
            Swal.fire({
                title: "¿Confirma cerrar la sesión en este momento?",
                text: "Se redirigirá al login",
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Ok",
                cancelButtonText: "Cancelar",
                confirmButtonColor: "#d33",
                cancelButtonColor: "#3085d6",
                showLoaderOnConfirm: true,
                preConfirm: () => {
                    document.getElementById('logout-form').submit();
                },
                allowOutsideClick: false,
                allowEscapeKey: false,
            });
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
                    })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Error al cerrar la caja');
                        }
                        return Swal.fire({
                            title: "Caja cerrada con éxito",
                            icon: "success",
                        });
                    })
                    .then(() => {
                        return Swal.fire({
                            title: "¿Desea cerrar sesión?",
                            icon: "question",
                            showCancelButton: true,
                            confirmButtonText: "Sí",
                            cancelButtonText: "No",
                        });
                    })
                    .then((result) => {
                        if (result.isConfirmed) {
                            document.getElementById('logout-form').submit();
                        }
                        else{
                            window.location.href = '/menu/';
                        }
                    });
                },
                allowOutsideClick: false,
                allowEscapeKey: false,
            });
        });
    }

    function getCsrfToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
    }
});
