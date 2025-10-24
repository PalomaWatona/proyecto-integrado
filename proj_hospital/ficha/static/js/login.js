
document.getElementById('rut').addEventListener('input', function (e) {
    let raw = e.target.value
        .replace(/\./g, '')       // Quita los puntos
        .replace(/-/g, '')        // Quita el guion
        .replace(/[^0-9kK]/g, '') // Solo permite dígitos y K/k
        .toUpperCase();           // Convierte la K en mayúscula

    if (raw.length > 1) {
        let cuerpo = raw.slice(0, -1);
        let dv = raw.slice(-1);
        cuerpo = cuerpo.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
        e.target.value = `${cuerpo}-${dv}`;
    } else {
        e.target.value = raw;
    }
});

document.getElementById('togglePassword').addEventListener('click', function () {
    const passwordInput = document.getElementById('password');
    const isHidden = passwordInput.type === 'password';
    passwordInput.type = isHidden ? 'text' : 'password';
});