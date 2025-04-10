document.addEventListener('DOMContentLoaded', () => {
  // ✅ Добавление в корзину
  document.querySelectorAll('.add-to-cart-btn').forEach(button => {
    button.addEventListener('click', function () {
      const productId = this.dataset.productId;

      fetch('/products/add-to-cart/', {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCookie('csrftoken'),
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `product_id=${productId}`
      })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          const counter = document.getElementById('cart-count');
          if (counter) {
            let current = parseInt(counter.textContent) || 0;
            counter.textContent = current + 1;
          }
          showToast(data.message);
        } else {
          showToast('Ошибка при добавлении в корзину', true);
        }
      });
    });
  });

  // ✅ Изменение количества товара ( + / - )
  document.querySelectorAll('.quantity-btn').forEach(button => {
    button.addEventListener('click', function () {
      const itemId = this.dataset.itemId;
      const action = this.dataset.action;

      fetch('/products/update-cart/', {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCookie('csrftoken'),
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `item_id=${itemId}&action=${action}`
      })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          window.location.reload();
        } else {
          showToast('Ошибка при обновлении корзины', true);
        }
      });
    });
  });

  // ✅ Удаление товара
  document.querySelectorAll('.remove-item').forEach(button => {
    button.addEventListener('click', function () {
      const itemId = this.dataset.itemId;

      fetch('/products/remove-from-cart/', {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCookie('csrftoken'),
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `item_id=${itemId}`
      })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          window.location.reload();
        } else {
          showToast('Ошибка при удалении товара', true);
        }
      });
    });
  });
});

// 💬 Уведомление
function showToast(message, isError = false) {
  const toast = document.getElementById('cart-toast');
  toast.textContent = message;
  toast.style.backgroundColor = isError ? '#dc3545' : '#28a745';
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 3000);
}

// 🔐 Получение CSRF-токена
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}