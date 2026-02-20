# 📖 ГЛАВА 3: JAVASCRIPT - ИНТЕРАКТИВНОСТЬ И ДИНАМИКА

## 🎯 Цель этой главы
Ты поймёшь:
- Как работает JavaScript в браузере
- Как реагировать на действия пользователя (клики, вводы)
- Что такое асинхронные операции
- Как AJAX позволяет обновлять страницу без перезагрузки

---

## 🚀 ЧАСТЬ 1: ОСНОВЫ JAVASCRIPT

### Где и как работает JavaScript?

```
🖥️ Сервер (Python/Flask) — обрабатывает запросы
                    ↓↑ HTTP
📱 Браузер (JavaScript) — выполняется на компьютере пользователя
```

JavaScript выполняется в браузере пользователя. Он может:
- Реагировать на клики мышки
- Изменять содержимое страницы
- Отправлять запросы на сервер
- Проверять форму ДО отправки на сервер

### Подключение JavaScript

```html
<!-- Способ 1: Внутри HTML -->
<script>
  console.log("Привет мир!");
</script>

<!-- Способ 2: Внешний файл (правильный способ) -->
<script src="script.js"></script>

<!-- Обычно подключаем в конце body -->
<body>
  <h1>HTML контент</h1>
  <script src="/static/js/script.js"></script>
</body>
```

### Консоль браузера

```javascript
console.log("Обычное сообщение");
console.error("Ошибка!");
console.warn("Предупреждение!");
```

Открыть консоль в браузере:
- Chrome/Edge: `F12` → вкладка Console
- Firefox: `F12` → вкладка Console

---

## 📝 ЧАСТЬ 2: ПЕРЕМЕННЫЕ И ТИПЫ ДАННЫХ

### Объявление переменных

```javascript
// var - старый способ (не используй)
var name = "Иван";

// let - современный способ (используй это)
let message = "Привет";
message = "Новое сообщение";  // Можно изменять

// const - постоянная (не меняется)
const maxItems = 100;
// maxItems = 200;  // ОШИБКА! Нельзя менять const
```

### Типы данных

```javascript
// Строки (текст)
let text = "Привет";
let text2 = 'Со одинарными кавычками';
let text3 = `С обратными кавычками (шаблон)`;

// Числа
let count = 42;
let price = 99.99;

// Булевы (true/false)
let isAdmin = true;
let isActive = false;

// Объекты (словари)
let user = {
  name: "Иван",
  age: 30,
  email: "ivan@example.com"
};
console.log(user.name);       // "Иван"
console.log(user['email']);   // "ivan@example.com"

// Массивы (списки)
let cars = ["BMW", "Mercedes", "Audi"];
cars.push("Toyota");  // Добавить в конец
console.log(cars[0]); // "BMW"

// null и undefined
let nothing = null;       // Пусто по нашему выбору
let unknown;              // undefined (не инициализировано)
```

### Операции с строками

```javascript
let hello = "Привет";
let name = "Иван";

// Объединение (конкатенация)
let message = hello + " " + name;  // "Привет Иван"

// Шаблонные строки (лучший способ)
let message2 = `${hello} ${name}`;  // "Привет Иван"

// Методы строк
"HELLO".toLowerCase();       // "hello"
"hello".toUpperCase();       // "HELLO"
"  hello  ".trim();          // "hello" (убрать пробелы)
"hello".includes("ell");     // true
"hello".replace("h", "H");   // "Hello"
```

---

## 🔄 ЧАСТЬ 3: ЦИКЛЫ И УСЛОВИЯ

### Условия (if/else)

```javascript
let age = 25;

if (age < 18) {
    console.log("Ты несовершеннолетний");
} else if (age >= 18 && age < 65) {
    console.log("Ты взрослый");
} else {
    console.log("Ты пенсионер");
}

// Тернарный оператор (условие в одну линию)
let status = age >= 18 ? "взрослый" : "ребёнок";
```

### Циклы

```javascript
// for - в цикле с индексом
for (let i = 0; i < 3; i++) {
    console.log(i);  // 0, 1, 2
}

// while - пока условие верно
let count = 0;
while (count < 5) {
    console.log(count);  // 0, 1, 2, 3, 4
    count++;
}

// forEach - для массивов
let fruits = ["яблоко", "банан", "апельсин"];
fruits.forEach((fruit, index) => {
    console.log(index, fruit);
});

// map - преобразовать каждый элемент
let prices = [100, 200, 300];
let doubled = prices.map(price => price * 2);  // [200, 400, 600]

// filter - оставить только подходящие
let numbers = [1, 2, 3, 4, 5];
let evens = numbers.filter(n => n % 2 === 0);  // [2, 4]
```

---

## 👆 ЧАСТЬ 4: СОБЫТИЯ И ОБРАБОТЧИКИ

### События браузера

**Клик:**
```html
<button id="my-button">Нажми меня</button>

<script>
  let button = document.getElementById("my-button");
  
  // Способ 1: addEventListener (правильный способ)
  button.addEventListener("click", function() {
    alert("Ты нажал на кнопку!");
  });
  
  // Способ 2: стрелочная функция (современнее)
  button.addEventListener("click", () => {
    console.log("Клик!");
  });
</script>
```

**Ввод текста:**
```html
<input type="text" id="search-box" placeholder="Искать...">

<script>
  let searchBox = document.getElementById("search-box");
  
  // Срабатывает когда пользователь печатает
  searchBox.addEventListener("input", (event) => {
    let query = event.target.value;
    console.log("Ты печатаешь:", query);
  });
</script>
```

**Отправка формы:**
```html
<form id="my-form">
  <input type="text" name="email" required>
  <button type="submit">Отправить</button>
</form>

<script>
  let form = document.getElementById("my-form");
  
  form.addEventListener("submit", (event) => {
    event.preventDefault();  // Не перезагружаем страницу!
    
    let email = form.email.value;  // Получить значение input
    console.log("Email:", email);
    
    // Отправить на сервер (смотри AJAX ниже)
  });
</script>
```

**Наведение мышки:**
```javascript
element.addEventListener("mouseover", () => {
    console.log("Мышка над элементом");
});

element.addEventListener("mouseleave", () => {
    console.log("Мышка ушла");
});
```

### Основные события

| Событие | Когда срабатывает |
|---------|------------------|
| `click` | Клик мышки |
| `dblclick` | Двойной клик |
| `input` | Ввод текста в поле |
| `change` | Изменили значение (и ушли из поля) |
| `submit` | Отправка формы |
| `load` | Страница загрузилась |
| `scroll` | Скролл страницы |
| `resize` | Изменена ширина окна |

---

## 🔍 ЧАСТЬ 5: РАБОТА С DOM (ДОКУМЕНТОМ)

### DOM (Document Object Model)

DOM - это представление HTML страницы в виде дерева объектов, которыми можно манипулировать:

```
document
├── html
│   ├── head
│   │   ├── title
│   │   └── meta
│   └── body
│       ├── h1
│       ├── div
│       └── script
```

### Поиск элементов

```javascript
// По ID (самый быстрый)
let element = document.getElementById("my-id");

// По тегу
let allParagraphs = document.getElementsByTagName("p");

// По классу
let cards = document.getElementsByClassName("card");

// Современные способы (селекторы как в CSS)
let element1 = document.querySelector("#my-id");          // Первый элемент
let element2 = document.querySelector(".card");           // Класс
let allCards = document.querySelectorAll(".card");        // Все элементы

// Перебор результатов
allCards.forEach(card => {
    console.log(card.textContent);
});
```

### Изменение содержимого

```javascript
let element = document.getElementById("my-element");

// Изменить только текст
element.textContent = "Новый текст";

// Изменить HTML (осторожнее!)
element.innerHTML = "<strong>Жирный текст</strong>";

// Добавить в конец
element.innerHTML += "<p>Добавленный текст</p>";

// Удалить элемент
element.remove();
```

### Изменение стилей

```javascript
let button = document.querySelector("button");

// Способ 1: Прямое изменение
button.style.backgroundColor = "blue";
button.style.color = "white";
button.style.padding = "10px 20px";

// Способ 2: Добавить класс (лучше)
button.classList.add("primary-button");

// Способ 3: Переключить класс
button.classList.toggle("active");

// Удалить класс
button.classList.remove("active");

// Проверить есть ли класс
if (button.classList.contains("active")) {
    console.log("Кнопка активна");
}
```

**CSS файл:**
```css
.primary-button {
    background: blue;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

.primary-button:hover {
    background: darkblue;
}
```

---

## 🌐 ЧАСТЬ 6: AJAX - АСИНХРОННЫЕ ЗАПРОСЫ

### Что такое асинхронность?

```
Синхронно (плохо):
  Запрос → Ждём ответ (страница заморожена) → Ответ → Продолжаем
  
Асинхронно (хорошо):
  Запрос → Продолжаем работать
  (когда приходит ответ) → обработать данные
```

### Fetch API (современный способ AJAX)

**Простой GET запрос:**
```javascript
// Получить список новостей с сервера
fetch("/api/news")
    .then(response => response.json())  // Преобразовать в JSON
    .then(data => {
        console.log("Новости получены:", data);
        displayNews(data);    // Показать новости
    })
    .catch(error => {
        console.error("Ошибка:", error);
    });
```

**POST запрос (отправить данные):**
```javascript
// Добавить новую новость
let newsData = {
    title: "Заголовок",
    source: "BBC"
};

fetch("/api/news", {
    method: "POST",                    // Тип запроса
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(newsData)    // Преобразовать объект в JSON строку
})
.then(response => response.json())
.then(data => {
    console.log("Новость добавлена:", data);
})
.catch(error => {
    console.error("Ошибка при добавлении:", error);
});
```

**С повтором попыток:**
```javascript
async function loadNews() {
    try {
        // await говорит: "жди ответа перед тем как идти дальше"
        let response = await fetch("/api/news");
        
        if (!response.ok) {
            throw new Error(`Ошибка ${response.status}`);
        }
        
        let data = await response.json();
        displayNews(data);
        
    } catch (error) {
        console.error("Ошибка при загрузке новостей:", error);
        alert("Не удалось загрузить новости");
    }
}

// Вызвать функцию
loadNews();
```

### Пример: Live Search

```html
<input type="text" id="search-box" placeholder="Поиск новостей">
<div id="results"></div>

<script>
  let searchBox = document.getElementById("search-box");
  let resultsDiv = document.getElementById("results");
  
  searchBox.addEventListener("input", async (event) => {
    let query = event.target.value.trim();
    
    if (query.length < 2) {
      resultsDiv.innerHTML = "";
      return;
    }
    
    try {
      // Отправить запрос на поиск
      let response = await fetch(`/api/search?q=${query}`);
      let results = await response.json();
      
      // Показать результаты
      resultsDiv.innerHTML = results
        .map(news => `
          <div class="result-card">
            <h3>${news.title}</h3>
            <p>${news.description}</p>
          </div>
        `)
        .join("");
        
    } catch (error) {
      console.error("Ошибка поиска:", error);
    }
  });
</script>
```

### Пример: Загрузка файлов через AJAX

```html
<input type="file" id="file-input">
<button id="upload-btn">Загрузить</button>
<div id="upload-status"></div>

<script>
  let uploadBtn = document.getElementById("upload-btn");
  let fileInput = document.getElementById("file-input");
  let statusDiv = document.getElementById("upload-status");
  
  uploadBtn.addEventListener("click", async () => {
    let file = fileInput.files[0];
    
    if (!file) {
      alert("Выбери файл!");
      return;
    }
    
    // Создать объект FormData для отправки файла
    let formData = new FormData();
    formData.append("file", file);
    
    statusDiv.textContent = "Загружаю...";
    
    try {
      let response = await fetch("/api/upload", {
        method: "POST",
        body: formData  // Важно! Не добавляй Content-Type, браузер сделает сам
      });
      
      let result = await response.json();
      statusDiv.textContent = "Загружено успешно!";
      
    } catch (error) {
      statusDiv.textContent = "Ошибка загрузки!";
      console.error(error);
    }
  });
</script>
```

---

## 💡 ЧАСТЬ 7: ПРАКТИЧЕСКИЕ ПРИМЕРЫ

### Пример 1: Модальное окно

```html
<!-- HTML -->
<button id="open-modal">Открыть</button>

<div id="modal" class="modal">
  <div class="modal-content">
    <span id="close-btn" class="close">&times;</span>
    <h2>Заголовок</h2>
    <p>Содержимое модального окна</p>
    <button id="confirm-btn">Подтвердить</button>
  </div>
</div>

<!-- CSS -->
<style>
.modal {
  display: none;              /* По умолчанию скрыто */
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);  /* Полупрозрачный фон */
}

.modal.show {
  display: flex;              /* Показать */
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 30px;
  border-radius: 10px;
  width: 90%;
  max-width: 500px;
}

.close {
  float: right;
  cursor: pointer;
  font-size: 28px;
  font-weight: bold;
}
</style>

<!-- JavaScript -->
<script>
let modal = document.getElementById("modal");
let openBtn = document.getElementById("open-modal");
let closeBtn = document.getElementById("close-btn");
let confirmBtn = document.getElementById("confirm-btn");

openBtn.addEventListener("click", () => {
  modal.classList.add("show");
});

closeBtn.addEventListener("click", () => {
  modal.classList.remove("show");
});

confirmBtn.addEventListener("click", () => {
  console.log("Подтвердили!");
  modal.classList.remove("show");
});

// Закрыть при клике на фон
modal.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.classList.remove("show");
  }
});
</script>
```

### Пример 2: Валидация формы с AJAX

```html
<form id="register-form">
  <input type="email" id="email" placeholder="Email" required>
  <span id="email-error" class="error"></span>
  
  <input type="password" id="password" placeholder="Пароль" required>
  
  <button type="submit">Зарегистрироваться</button>
  <div id="status"></div>
</form>

<script>
let form = document.getElementById("register-form");
let emailInput = document.getElementById("email");
let emailError = document.getElementById("email-error");
let statusDiv = document.getElementById("status");

// Проверка email при вводе
emailInput.addEventListener("change", async () => {
  let email = emailInput.value;
  
  try {
    let response = await fetch(`/api/check-email?email=${email}`);
    let result = await response.json();
    
    if (result.exists) {
      emailError.textContent = "Этот email уже зарегистрирован!";
      emailError.style.color = "red";
    } else {
      emailError.textContent = "Email доступен!";
      emailError.style.color = "green";
    }
  } catch (error) {
    console.error(error);
  }
});

// Отправка формы
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  
  let email = emailInput.value;
  let password = document.getElementById("password").value;
  
  statusDiv.textContent = "Регистрируюсь...";
  
  try {
    let response = await fetch("/api/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ email, password })
    });
    
    let result = await response.json();
    
    if (response.ok) {
      statusDiv.textContent = "Успешно зарегистрирован!";
      statusDiv.style.color = "green";
      form.reset();
    } else {
      statusDiv.textContent = result.error || "Ошибка регистрации";
      statusDiv.style.color = "red";
    }
  } catch (error) {
    statusDiv.textContent = "Ошибка связи с сервером";
    statusDiv.style.color = "red";
  }
});
</script>
```

---

## 🎓 ИТОГИ

После этой главы ты знаешь:
- ✅ Как работает JavaScript в браузере
- ✅ Переменные, типы данных, операции
- ✅ Условия и циклы
- ✅ События (клики, вводы текста и т.д.)
- ✅ Как работать с DOM
- ✅ Fetch API для асинхронных запросов (AJAX)
- ✅ Практические примеры: модали, формы, поиск

**Вечером на практике ты:**
- Создашь интерактивные элементы
- Свяжешь кнопки с действиями
- Отправишь данные на сервер через AJAX
- Обновишь страницу без перезагрузки
- Создашь валидацию форм

---

**Помни:** JavaScript это то что делает сайт "живым"! 🚀
