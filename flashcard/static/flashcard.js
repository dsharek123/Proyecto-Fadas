const contenedor = document.querySelector(".container");
const agregarTarjetaContainer = document.getElementById("add-question-card");
const botonGuardar = document.getElementById("save-btn");
const inputPregunta = document.getElementById("question");
const inputRespuesta = document.getElementById("answer");
const mensajeError = document.getElementById("error");
const botonAgregarTarjeta = document.getElementById("add-flashcard");
const botonCerrar = document.getElementById("close-btn");
const modalTitle = document.getElementById("modal-title");

// Elementos del formulario principal
const mainForm = document.getElementById('main-form');
const hiddenPregunta = document.getElementById('hidden-pregunta');
const hiddenRespuesta = document.getElementById('hidden-respuesta');
const hiddenAction = document.getElementById('hidden-action');
const hiddenCardId = document.getElementById('hidden-card-id');

let enEdicion = false;
let tarjetaEditandoId = null;

// Mostrar formulario para crear
botonAgregarTarjeta.addEventListener("click", () => {
  console.log("📝 Abriendo modal para crear flashcard");
  contenedor.classList.add("hide");
  inputPregunta.value = "";
  inputRespuesta.value = "";
  agregarTarjetaContainer.classList.remove("hide");
  enEdicion = false;
  tarjetaEditandoId = null;
  modalTitle.textContent = "Crear Flashcard";
});

// Cerrar formulario
botonCerrar.addEventListener("click", ocultarFormulario);

function ocultarFormulario() {
  console.log("❌ Cerrando modal");
  contenedor.classList.remove("hide");
  agregarTarjetaContainer.classList.add("hide");
  if (enEdicion) {
    enEdicion = false;
    tarjetaEditandoId = null;
  }
}

// Guardar flashcard - SOLO ENVIA A DJANGO
botonGuardar.addEventListener("click", enviarTarjeta);

function enviarTarjeta() {
  let tempPregunta = inputPregunta.value.trim();
  let tempRespuesta = inputRespuesta.value.trim();
  
  console.log("💾 Intentando guardar flashcard:", { tempPregunta, tempRespuesta });
  
  if (!tempPregunta || !tempRespuesta) {
    console.log("❌ Campos vacíos, mostrando error");
    mensajeError.classList.remove("hide");
  } else {
    console.log("✅ Campos válidos, enviando a Django");
    mensajeError.classList.add("hide");
    
    // SOLO ENVIA A DJANGO - NO crees tarjetas en el frontend
    if (enEdicion && tarjetaEditandoId) {
      console.log("✏️ Modo edición para tarjeta ID:", tarjetaEditandoId);
      enviarADjango(tempPregunta, tempRespuesta, 'edit', tarjetaEditandoId);
    } else {
      console.log("🆕 Modo creación");
      enviarADjango(tempPregunta, tempRespuesta, 'create');
    }
    
    // NO limpies inputs - Django redirigirá y recargará la página
    // NO muestres tarjetas - Django las renderizará desde la BD
    // NO ocultes formulario - Django redirigirá
  }
}

// Función para enviar datos a Django
function enviarADjango(pregunta, respuesta, action, cardId = null) {
  console.log("🚀 Enviando a Django:", { pregunta, respuesta, action, cardId });
  
  hiddenPregunta.value = pregunta;
  hiddenRespuesta.value = respuesta;
  hiddenAction.value = action;
  
  if (cardId) {
    hiddenCardId.value = cardId;
  } else {
    hiddenCardId.value = '';
  }
  
  // Esto recargará la página con los datos actualizados
  mainForm.submit();
}

// Inicializar eventos cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
  console.log("🔧 Inicializando eventos de flashcards existentes");
  
  // Mostrar/ocultar respuesta
  document.querySelectorAll('.show-hide-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      const card = this.closest('.card');
      const answerDiv = card.querySelector('.answer-div');
      answerDiv.classList.toggle('hide');
      console.log("👁️ Mostrar/ocultar respuesta");
    });
  });

  // Editar flashcard
  document.querySelectorAll('.edit').forEach(btn => {
    btn.addEventListener('click', function() {
      const cardId = this.getAttribute('data-id');
      const card = this.closest('.card');
      const pregunta = card.querySelector('.question-div').innerText;
      const respuesta = card.querySelector('.answer-div').innerText;
      
      console.log("✏️ Editando flashcard ID:", cardId);
      
      inputPregunta.value = pregunta;
      inputRespuesta.value = respuesta;
      enEdicion = true;
      tarjetaEditandoId = cardId;
      modalTitle.textContent = "Editar Flashcard";
      
      contenedor.classList.add("hide");
      agregarTarjetaContainer.classList.remove("hide");
    });
  });

  // Eliminar flashcard
  document.querySelectorAll('.delete').forEach(btn => {
    btn.addEventListener('click', function() {
      const cardId = this.getAttribute('data-id');
      console.log("🗑️ Intentando eliminar flashcard ID:", cardId);
      
      if (confirm('¿Estás seguro de eliminar esta flashcard?')) {
        console.log("✅ Confirmado, eliminando...");
        enviarADjango('', '', 'delete', cardId);
      } else {
        console.log("❌ Eliminación cancelada");
      }
    });
  });
});

