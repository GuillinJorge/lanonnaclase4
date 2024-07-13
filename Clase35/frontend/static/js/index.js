/**
 * Script para gestionar las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) de películas
 * a través de una API REST usando fetch y el patrón MVC.
 * 
 * Variables:
 * - form: Referencia al formulario para crear nuevas películas.
 * - btn: Referencia al botón de creación de películas.
 * - successMessage: Referencia al mensaje de éxito que se muestra al crear una película.
 * - URL_API_BASE: URL base de la API de películas.
 * 
 * Eventos:
 * - Click en el botón de creación de películas.
 * - Click en el botón de mostrar películas.
 * 
 * Clases:
 * - Pelicula: Representa una película y contiene métodos para generar su HTML.
 * 
 * Funciones:
 * - fetchPeliculas: Obtiene y muestra la lista de películas desde la API.
 * - deletePelicula: Elimina una película específica mediante su ID.
 * - toggleEditForm: Muestra u oculta el formulario de edición de una película.
 * - editPelicula: Envía los datos editados de una película a la API.
 */

const form = document.getElementById("crear_pelicula_form");
const btn = document.getElementById("btn-post");
const successMessage = document.getElementById("success-message");
const URL_API_BASE = "http://127.0.0.1:8000/api/pelicula/";

// Evento para manejar la creación de una nueva película
btn.addEventListener("click", (e) => {
    e.preventDefault();
    fetch(URL_API_BASE, {
        method: 'POST',
        body: new FormData(form)
    })
    .then(res => res.json())
    .then(data => {
        // Mostrar mensaje de éxito
        successMessage.style.display = 'block';
        // Limpiar formulario
        form.reset();
        // Ocultar mensaje después de 3 segundos
        setTimeout(() => {
            successMessage.style.display = 'none';
        }, 3000);
        // Actualizar la lista de películas
        fetchPeliculas();
    })
    .catch(error => console.log({error}));
});

// Clase para representar una película y generar su HTML
class Pelicula {
    constructor({fecha_release, genero, id, nombre, duracion}) {
        this.fecha_release = fecha_release;
        this.genero = genero;
        this.id = id;
        this.nombre = nombre;
        this.duracion = duracion;
    }

    createDiv() {
        return `
            <div id="pelicula-${this.id}">
                <h4>${this.nombre}</h4>
                <hr>
                <ul>
                    <li>Duración: ${this.duracion}</li>
                    <li>Género: ${this.genero}</li>
                    <li>Fecha de lanzamiento: ${this.fecha_release}</li>
                </ul>
                <div class="boton-container">
                    <button onclick="deletePelicula(${this.id})">Eliminar</button>
                    <button onclick="toggleEditForm(${this.id})">Editar</button>
                </div>
                <form id="edit-form-${this.id}" style="display: none;">
                    <label>Nombre:</label>
                    <input type="text" id="edit-nombre-${this.id}" value="${this.nombre}"><br>
                    <label>Duración:</label>
                    <input type="text" id="edit-duracion-${this.id}" value="${this.duracion}"><br>
                    <label>Género:</label>
                    <select id="edit-genero-${this.id}">
                        <option value="accion" ${this.genero === 'accion' ? 'selected' : ''}>Acción</option>
                        <option value="comedia" ${this.genero === 'comedia' ? 'selected' : ''}>Comedia</option>
                        <option value="drama" ${this.genero === 'drama' ? 'selected' : ''}>Drama</option>
                        <option value="infantil" ${this.genero === 'infantil' ? 'selected' : ''}>Infantil</option>
                        <option value="terror" ${this.genero === 'terror' ? 'selected' : ''}>Terror</option>
                        <option value="animacion" ${this.genero === 'animacion' ? 'selected' : ''}>Animación</option>
                        <option value="suspenso" ${this.genero === 'suspenso' ? 'selected' : ''}>Suspenso</option>
                        <option value="ciencia_ficcion" ${this.genero === 'ciencia_ficcion' ? 'selected' : ''}>Ciencia Ficción</option>
                    </select><br>
                    <label>Fecha de lanzamiento:</label>
                    <input type="date" id="edit-fecha_release-${this.id}" value="${this.fecha_release}"><br>
                    <button type="button" onclick="editPelicula(${this.id})">Guardar cambios</button>
                </form>
            </div>
        `;
    }
}

const btnGet = document.getElementById("btn-get");

// Evento para manejar la obtención de la lista de películas
btnGet.addEventListener("click", fetchPeliculas);

// Función para obtener y mostrar la lista de películas
function fetchPeliculas() {
    fetch(URL_API_BASE)
    .then(res => res.json())
    .then(data => {
        const ingesta_data = data
            .map(p => new Pelicula(p))
            .map(pelicula => pelicula.createDiv())
            .join('');

        document.getElementById("peliculas").innerHTML = ingesta_data;
    })
    .catch(error => console.log({error}));
}

// Función para eliminar una película específica mediante su ID
function deletePelicula(id) {
    fetch(`${URL_API_BASE}${id}/`, {
        method: 'DELETE'
    })
    .then(() => {
        fetchPeliculas(); // Actualiza la lista de películas después de eliminar una
    })
    .catch(error => console.log({error}));
}

// Función para mostrar u ocultar el formulario de edición de una película
function toggleEditForm(id) {
    const form = document.getElementById(`edit-form-${id}`);
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
}

// Función para enviar los datos editados de una película a la API
function editPelicula(id) {
    const nombre = document.getElementById(`edit-nombre-${id}`).value;
    const duracion = document.getElementById(`edit-duracion-${id}`).value;
    const genero = document.getElementById(`edit-genero-${id}`).value;
    const fecha_release = document.getElementById(`edit-fecha_release-${id}`).value;

    fetch(`${URL_API_BASE}${id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nombre,
            duracion,
            genero,
            fecha_release
        })
    })
    .then(() => {
        fetchPeliculas(); // Actualiza la lista de películas después de editar una
    })
    .catch(error => console.log({error}));
}
