// URL de la API
const API_URL = "http://127.0.0.1:5000/api/products";

// Elemento donde se mostrarán los productos
const productList = document.getElementById("product-list");

// Función para obtener los productos de la API
async function fetchProducts() {
  try {
    const response = await fetch(API_URL);
    const products = await response.json();
    renderProducts(products);
  } catch (error) {
    console.error("Error fetching products:", error);
  }
}

// Función para renderizar los productos en la página
function renderProducts(products) {
  productList.innerHTML = ""; // Limpiar la lista
  products.forEach(product => {
    const listItem = document.createElement("li");
    listItem.textContent = `${product.name} - $${product.price}`;
    productList.appendChild(listItem);
  });
}

// Llamar a la función al cargar la página
fetchProducts();
