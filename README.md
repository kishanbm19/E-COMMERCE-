# E-COMMERCE-
E-Commerce Backend API (Django + DRF + MySQL)

A backend E-Commerce REST API built using Django, Django REST Framework, and MySQL. This project provides APIs for managing products, categories, carts, and orders.

🚀 Features
User Authentication (Django User Model)
Product & Category Management
Shopping Cart System
Order Management
Discount Price Calculation
MySQL Database Integration
RESTful APIs with Django REST Framework
🛠️ Tech Stack
Python
Django
Django REST Framework
MySQL




📂 Models
Category: Product categories
Product: Title, price, description, discount, final price
Cart: User cart
CartItem: Product + quantity + total price
Order: User orders with status
OrderItem: Ordered products + final price
🔗 API Endpoints
/categories/
/products/
/cart/
/cartitems/
/Order/
/orderitems/



🗄️ MySQL Configuration

Update settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}



📈 Future Improvements
JWT Authentication
Payment Gateway
Wishlist
Reviews & Ratings
Order Tracking
Admin Dashboard
Soon after I learn frontend It will be integrated with it.



👨‍💻 Author
Kishan BM


