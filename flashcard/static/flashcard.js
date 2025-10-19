const contenedor = document.querySelector(".container");
const agregarTarjetaContainer = document.getElementById("add-question-card");
const botonGuardar = document.getElementById("save-btn");
const inputPregunta = document.getElementById("question");
const inputRespuesta = document.getElementById("answer");
const mensajeError = document.getElementById("error");
const botonAgregarTarjeta = document.getElementById("add-flashcard");
const botonCerrar = document.getElementById("close-btn");
let enEdicion = false;

botonAgregarTarjeta.addEventListener("click", () => {
  contenedor.classList.add("hide");
  inputPregunta.value = "";
  inputRespuesta.value = "";
  agregarTarjetaContainer.classList.remove("hide");
});

botonCerrar.addEventListener(
  "click",
  (ocultarFormulario = () => {
    contenedor.classList.remove("hide");
    agregarTarjetaContainer.classList.add("hide");
    if (enEdicion) {
      enEdicion = false;
      enviarTarjeta();
    }
  })
);

botonGuardar.addEventListener(
  "click",
  (enviarTarjeta = () => {
    enEdicion = false;
    let tempPregunta = inputPregunta.value.trim();
    let tempRespuesta = inputRespuesta.value.trim();
    guardarEnLocalStorage(tempPregunta, tempRespuesta);
    
    if (!tempPregunta || !tempRespuesta) {
      mensajeError.classList.remove("hide");
    } else {
      contenedor.classList.remove("hide");
      mensajeError.classList.add("hide");
      mostrarTarjetas();
      inputPregunta.value = "";
      inputRespuesta.value = "";
    }
  })
);

function mostrarTarjetas() {
  const listaTarjetas = document.getElementsByClassName("card-list-container");
  const tarjetaDiv = document.createElement("div");
  tarjetaDiv.classList.add("card");

  tarjetaDiv.innerHTML += `<p class="question-div">${inputPregunta.value}</p>`;

  const respuestaDiv = document.createElement("p");
  respuestaDiv.classList.add("answer-div", "hide");
  respuestaDiv.innerText = inputRespuesta.value;

  const botonMostrar = document.createElement("a");
  botonMostrar.setAttribute("href", "#");
  botonMostrar.setAttribute("class", "show-hide-btn");
  botonMostrar.innerHTML = "Mostrar/Ocultar Respuesta";
  botonMostrar.addEventListener("click", () => {
    respuestaDiv.classList.toggle("hide");
  });
  tarjetaDiv.appendChild(botonMostrar);
  tarjetaDiv.appendChild(respuestaDiv);

  const contBotones = document.createElement("div");
  contBotones.classList.add("buttons-con");

  const botonEditar = document.createElement("button");
  botonEditar.setAttribute("class", "edit");
  botonEditar.innerHTML = `<i class="fa-solid fa-pen-to-square"></i>`;
  botonEditar.addEventListener("click", () => {
    enEdicion = true;
    modificarElemento(botonEditar, true);
    agregarTarjetaContainer.classList.remove("hide");
  });
  contBotones.appendChild(botonEditar);
  deshabilitarBotones(false);

  const botonEliminar = document.createElement("button");
  botonEliminar.setAttribute("class", "delete");
  botonEliminar.innerHTML = `<i class="fa-solid fa-trash-can"></i>`;
  botonEliminar.addEventListener("click", () => {
    modificarElemento(botonEliminar);
  });
  contBotones.appendChild(botonEliminar);

  tarjetaDiv.appendChild(contBotones);
  listaTarjetas[0].appendChild(tarjetaDiv);

  ocultarFormulario();
}

const modificarElemento = (elemento, editar = false) => {
  const tarjetaPadre = elemento.parentElement.parentElement;
  const textoPregunta = tarjetaPadre.querySelector(".question-div").innerText;

  if (editar) {
    const textoRespuesta = tarjetaPadre.querySelector(".answer-div").innerText;
    inputPregunta.value = textoPregunta;
    inputRespuesta.value = textoRespuesta;
    deshabilitarBotones(true);
  }

  tarjetaPadre.remove();
};

const deshabilitarBotones = (valor) => {
  const botonesEditar = document.getElementsByClassName("edit");
  Array.from(botonesEditar).forEach((elemento) => {
    elemento.disabled = valor;
  });
};
function guardarEnLocalStorage(pregunta, respuesta) {
  let flashcards = JSON.parse(localStorage.getItem("flashcards")) || [];
  flashcards.push({ pregunta, respuesta });
  localStorage.setItem("flashcards", JSON.stringify(flashcards));
}

