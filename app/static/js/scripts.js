document.addEventListener("DOMContentLoaded", function() {
    let mensajeElement = document.getElementById("mensaje");
    if (mensajeElement) {
        alert(mensajeElement.value);
    }
});

function agregarPropuesta() {
    var container = document.getElementById('propuestas-container');
    var newInputGroup = document.createElement('div');
    newInputGroup.className = 'input-group mb-3';
    
    var newInput = document.createElement('input');
    newInput.type = 'text';
    newInput.className = 'form-control';
    newInput.name = 'propuestas[]';
    newInput.placeholder = 'Propuesta';
    
    var newButtonDiv = document.createElement('div');
    newButtonDiv.className = 'input-group-append';
    
    var newButton = document.createElement('button');
    newButton.className = 'btn btn-outline-secondary';
    newButton.type = 'button';
    newButton.textContent = 'Añadir';
    newButton.onclick = agregarPropuesta;
    
    newButtonDiv.appendChild(newButton);
    newInputGroup.appendChild(newInput);
    newInputGroup.appendChild(newButtonDiv);
    container.appendChild(newInputGroup);
}
