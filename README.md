# 🛒 E-Commerce Backend API (Django + DRF + MySQL)

A **RESTful E-Commerce Backend API** built using **Django**, **Django REST Framework (DRF)**, and **MySQL**. The project provides secure APIs for user management, product catalog, shopping cart, and order processing. It supports CRUD operations, search, filtering, pagination, and automatic price calculations. All APIs were developed and tested using **Postman**.

---

# 📁 Project Structure

```text
backend/
├── product/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── routers.py
│   ├── serializers.py
│   ├── tests.py
│   └── viewsets.py
│
├── shopverse/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🚀 Features

- 👤 User Registration & Authentication
- 📦 Complete Product CRUD Operations
- 🗂️ Category Management
- 🛒 Shopping Cart Management
- 📋 Order & Order Item Management
- 💰 Automatic Discount, Total Price & Final Price Calculations
- 🗄️ MySQL Database Integration
- 🔗 RESTful APIs using Django REST Framework
- ⚡ ModelSerializers for JSON Serialization
- 🔄 RESTful CRUD APIs using DRF ModelViewSets & Routers
- 🔍 Product Search using DRF SearchFilter
- 🎯 Product Filtering using DjangoFilterBackend
- 📄 Pagination for Efficient API Responses
- 🧪 API Development & Testing using Postman
- 🛠️ Django Admin Panel

---

# 📌 API Capabilities

- 👤 User Registration & Authentication
- 📦 CRUD Operations
- 🔄 JSON Serialization
- 🔍 Search
- 🎯 Filtering
- 📄 Pagination
- 🔗 Foreign Key Relationships
- 🧮 Computed Properties (`final_price`, `total_price`)

---

# 🛠️ Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- MySQL
- Postman

---

# 📂 Database Models

### Category

Stores product categories.

**Fields**
- Category Name

---

### Product

Stores product information.

**Fields**
- Title
- Description
- Price
- Discount Percentage
- Category

**Computed Property**
- Final Price

---

### Cart

Represents a user's shopping cart.

**Fields**
- User

---

### CartItem

Represents products added to the shopping cart.

**Fields**
- Cart
- Product
- Quantity

**Computed Property**
- Total Price

---

### Order

Stores order information.

**Fields**
- User
- Order Status

---

### OrderItem

Stores ordered products.

**Fields**
- Order
- Product
- Quantity
- Discount

**Computed Properties**
- Total Price
- Final Price

---

# 🔗 Database Relationships

```text
Category
   │
   └──────< Product

User
   │
   └──────< Cart
                │
                └──────< CartItem

User
   │
   └──────< Order
                 │
                 └──────< OrderItem
```

---

# 🌐 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/categories/` | Category CRUD Operations |
| `/products/` | Product CRUD Operations |
| `/cart/` | Shopping Cart Management |
| `/cartitems/` | Manage Cart Items |
| `/orders/` | Order Management |
| `/orderitems/` | Order Item Management |

---

# ▶️ Application Workflow

```text
User Registration / Login
          │
          ▼
Browse Categories
          │
          ▼
View Products
          │
          ▼
Search & Filter Products
          │
          ▼
Add Products to Cart
          │
          ▼
Update Cart Items
          │
          ▼
Create Order
          │
          ▼
Calculate Total & Final Price
          │
          ▼
Store Order in MySQL Database
          │
          ▼
View Order Details
```

---

# 🚀 Future Improvements

- 🔐 JWT Authentication using Django REST Framework Simple JWT
- 💳 Payment Gateway Integration (Stripe/Razorpay)
- ❤️ Wishlist Management
- ⭐ Product Reviews & Ratings
- 📦 Order Tracking System
- 📧 Email Notifications
- 📈 Sales Analytics Dashboard
- 📄 Invoice Generation (PDF)
- 🏷️ Coupon & Promo Code Support
- 📂 Product Image Uploads
- 🌍 Role-Based Access Control (Admin, Seller & Customer)
- 🐳 Docker Containerization
- ☁️ Deployment on AWS, Render, or Railway
- 🌐 Frontend Integration using React or Next.js
- 📖 API Documentation using Swagger/OpenAPI
- 🧪 Unit & Integration Testing
- ⚡ Redis Caching for Improved Performance
