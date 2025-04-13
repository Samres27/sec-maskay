// static/js/escaneo.js
document.addEventListener('DOMContentLoaded', function() {
    // Referencias a elementos del DOM
    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');
    
    // Función para manejar la búsqueda
    function handleSearch() {
        const searchTerm = searchInput.value.trim();
        if (searchTerm) {
            console.log('Realizando búsqueda:', searchTerm);
            // Aquí puedes implementar la lógica de búsqueda
            // Por ejemplo, enviar una solicitud al backend de Flask
            // fetch('/api/search?term=' + encodeURIComponent(searchTerm))
            //     .then(response => response.json())
            //     .then(data => {
            //         // Procesar resultados
            //     });
        }
    }
    
    // Event listeners
    searchButton.addEventListener('click', handleSearch);
    
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            handleSearch();
        }
    });
});
