# 🛒 E-Commerce Backend API (Django + DRF + MySQL)

A **RESTful E-Commerce Backend API** built using **Django**, **Django REST Framework (DRF)**, and **MySQL**. The project provides APIs for user authentication, product management, shopping carts, and order processing. Alongside the REST APIs, the project also includes **Django Views, HTML templates, and static files** to render basic frontend pages for product browsing and management. All API endpoints were tested and validated using **Postman**.

---

# 📁 Project Structure

```text
ecommerce_backend/
├── ecommerce/                 # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── store/                     # Main application
│   ├── models.py              # Database models
│   ├── serializers.py         # DRF serializers
│   ├── views.py               # API views & Django template views
│   ├── urls.py                # URL routing
│   ├── admin.py               # Django admin configuration
│   ├── templates/             # HTML templates
│   ├── static/                # CSS, JavaScript & Images
│   └── migrations/            # Database migrations
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🚀 Features

* 👤 User Authentication using Django's built-in User Model
* 📦 Complete Product CRUD Operations
* 🗂️ Category Management
* 🛒 Shopping Cart with Quantity Management
* 📋 Order & Order Item Management
* 💰 Automatic Discount and Final Price Calculation
* 🗄️ MySQL Database Integration
* 🔗 RESTful APIs developed using Django REST Framework
* 🌐 Server-rendered frontend pages using Django Views and HTML Templates
* 🎨 Static file management for CSS, JavaScript, and Images
* 🧪 API Testing and Validation using Postman
* 🛠️ Django Admin Panel for easy data management

---

# 🛠️ Tech Stack

* Python
* Django
* Django REST Framework (DRF)
* MySQL
* Postman
* Django Template Engine

---

# 📂 Database Models

### Category

* Stores product categories.

### Product

* Product title
* Description
* Original price
* Discount percentage
* Automatically calculated final price
* Linked category

### Cart

* User's shopping cart.

### CartItem

* Product
* Quantity
* Total price

### Order

* User
* Order status
* Order date

### OrderItem

* Ordered product
* Quantity
* Final price

---

# 🔗 API Endpoints

| Endpoint       | Description              |
| -------------- | ------------------------ |
| `/categories/` | Category CRUD operations |
| `/products/`   | Product CRUD operations  |
| `/cart/`       | Shopping cart management |
| `/cartitems/`  | Manage cart items        |
| `/orders/`     | Create and manage orders |
| `/orderitems/` | View ordered products    |

---

# ▶️ Application Workflow

```text
User Registers / Login
          │
          ▼
Browse Categories
          │
          ▼
View Products
          │
          ▼
Add Products to Cart
          │
          ▼
Update Cart Quantity
          │
          ▼
Place Order
          │
          ▼
Order Saved in MySQL Database
          │
          ▼
View Order Details
```



