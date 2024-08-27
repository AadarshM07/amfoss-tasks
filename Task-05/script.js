fetch("https://fakestoreapi.com/products")
  .then((response) => response.json())
  .then((data) => {
    const items = data;
    renderProducts(items);

    const output = document.querySelector('.terminal-output');
    const inputField = document.querySelector('input[type="text"]');
    let shoppingCart = [];

    function processInput() {
      const userInput = inputField.value.trim().toLowerCase();
      const [cmd, ...parameters] = userInput.split(' ');

      if (cmd === 'help') {
        displayHelp();
      } else if (cmd === 'list') {
        showProducts();
      } else if (cmd === 'details') {
        showDetails(parameters[0]);
      } else if (cmd === 'add') {
        addItemToCart(parameters[0]);
      } else if (cmd === 'remove') {
        removeItemFromCart(parameters[0]);
      } else if (cmd === 'cart') {
        displayCart();
      } else if (cmd === 'buy') {
        checkout();
      } else if (cmd === 'clear') {
        clearTerminal();
      } else if (cmd === 'search') {
        findProduct(parameters.join(' '));
      } else if (cmd === 'sort') {
        arrangeProducts(parameters[0]);
      } else {
        output.textContent += `Unknown command: ${cmd}\n`;
      }

      inputField.value = '';
    }

    function displayHelp() {
      output.innerHTML += "Available Commands:\n1) help,\n2) list,\n3) details 'product_id',\n4) add 'product_id',\n5) remove 'product id',\n6) cart,\n7) buy,\n8) clear,\n9) search 'product_name',\n10) sort 'price/name'\n";
    }

    function showProducts() {
      for (let i = 0; i < items.length; i++) {
        let item = items[i];
        output.innerHTML += `ID: ${item.id}, Name: ${item.title}, Price: $${item.price}\n`;
      }
    }

    function showDetails(itemId) {
      const item = items.find(p => p.id == itemId);
      if (item) {
        output.innerHTML += `ID: ${item.id},\n Name: ${item.title},\n Price: $${item.price},\n Description: ${item.description}\n`;
      } else {
        output.innerHTML += `Item with ID ${itemId} not found.\n`;
      }
    }

    function addItemToCart(itemId) {
      let selectedItem = null;
      for (let i = 0; i < items.length; i++) {
        if (items[i].id == itemId) {
          selectedItem = items[i];
          break;
        }
      }

      if (selectedItem) {
        shoppingCart.push(selectedItem);
        output.innerHTML += `Added item with ID ${selectedItem.id} to the cart.\n`;
        recalculateCartTotal();
      } else {
        output.innerHTML += `Item with ID ${itemId} not found.\n`;
      }
    }

    function removeItemFromCart(itemId) {
      shoppingCart = shoppingCart.filter(item => item.id != itemId);
      output.innerHTML += `Removed item with ID ${itemId} from the cart.\n`;
      recalculateCartTotal();
    }

    function displayCart() {
      if (shoppingCart.length === 0) {
        output.innerHTML += "Your cart is empty.\n";
      } else {
        output.innerHTML += "Items in your cart:\n";
        shoppingCart.forEach(item => {
          output.innerHTML += `ID: ${item.id}, Name: ${item.title}, Price: $${item.price}, Description: ${item.description}\n`;
        });
      }
    }

    function checkout() {
      if (shoppingCart.length === 0) {
        output.innerHTML += "Your cart is empty. Add items to cart before proceeding to buy.\n";
      } else {
        sessionStorage.setItem('cart', JSON.stringify(shoppingCart));
        window.open('buy.html', '_blank');
      }
    }

    function clearTerminal() {
      output.innerHTML = '';
    }

    function findProduct(itemName) {
      let foundItem;
      for (const item of items) {
        if (item.title.toLowerCase().includes(itemName.trim().toLowerCase())) {
          foundItem = item;
          break;
        }
      }
      if (foundItem) {
        output.innerHTML += `Found: ID: ${foundItem.id}, Name: ${foundItem.title}, Price: $${foundItem.price}\n`;
      } else {
        output.innerHTML += `Product named '${itemName}' not found.\n`;
      }
    }

    function arrangeProducts(orderBy) {
      if (orderBy === 'price') {
        items.sort((a, b) => a.price - b.price);
      } else if (orderBy === 'name') {
        items.sort((a, b) => a.title.localeCompare(b.title));
      }

      const itemsContainer = document.getElementById("products");
      itemsContainer.innerHTML = '';
      renderProducts(items);

      items.forEach(item => {
        output.innerHTML += `ID: ${item.id}, Name: ${item.title}, Price: $${item.price}\n`;
      });
    }

    function recalculateCartTotal() {
      let total = 0;
      for (let i = 0; i < shoppingCart.length; i++) {
        total += shoppingCart[i].price;
      }
      const totalElement = document.getElementById('cart-price');
      totalElement.innerHTML = `$${total.toFixed(2)}`;
    }

    inputField.addEventListener('keydown', function(event) {
      if (event.key === 'Enter') {
        processInput();
      }
    });
  });

function renderProducts(products) {
  const container = document.getElementById("products");

  for (let i = 0; i < products.length; i++) {
    const item = products[i];

    const itemElement = document.createElement("div");
    itemElement.className = "product";

    const imageElement = document.createElement("img");
    imageElement.src = item.image;
    imageElement.alt = item.title;
    itemElement.appendChild(imageElement);

    const discountedPriceValue = item.price + 100;

    const favoriteIcon = document.createElement("i");
    favoriteIcon.className = "far fa-heart";
    favoriteIcon.style.float = "left";
    itemElement.appendChild(favoriteIcon);

    const discountedPrice = document.createElement("p");
    discountedPrice.className = "discounted-price";
    discountedPrice.innerText = `$${discountedPriceValue}`;
    discountedPrice.style.color = "red";
    discountedPrice.style.textDecoration = "line-through";
    itemElement.appendChild(discountedPrice);

    const actualPrice = document.createElement("p");
    actualPrice.className = "actual-price";
    actualPrice.innerText = `$${item.price}`;
    itemElement.appendChild(actualPrice);

    const cartIcon = document.createElement("i");
    cartIcon.className = "fas fa-shopping-cart";
    cartIcon.style.float = "right";
    itemElement.appendChild(cartIcon);

    container.appendChild(itemElement);
  }
}

