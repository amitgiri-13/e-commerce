# Django E-Commerce Platform

A modular and scalable e-commerce web application built with Django. It supports vendor and customer management, product listings, order processing, and REST APIs.

---

##  Features

*  **User Roles**: Vendor and Customer support with role-based permissions.
*  **Product Management**: Vendors can add and manage their products.
*  **Order System**: Customers can place orders; system tracks steps and order status.
*  **API Layer**: Modular API via Django REST Framework (DRF).
*  **Frontend**: Django templates used for store and vendor views.
*  **Client Scripts**: Simulate ordering and client-side behavior.
*  **Permissions**: Custom permissions for API access and actions.

---

##  Project Structure

```
.
├── api/          # API layer for external interaction
├── client/       # Scripts and logic to simulate frontend behavior
├── ecom/         # Project settings and URLs
├── store/        # Customer-facing logic: products, orders, templates
├── vendor/       # Vendor dashboard and management system
└── manage.py     # Django CLI entry point
```

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/django-ecom.git
cd django-ecom
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### 3. Run Migrations & Create Superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. Start Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to access the site.

---

##  Admin Panel

You can log into the Django admin panel at:

```
http://127.0.0.1:8000/admin/
```

Use the superuser credentials you created during setup.

---

##  API Endpoints

Basic endpoints provided by the `api/` app allow interaction via REST API.

* Example: `GET /api/products/`
* More routes can be added and documented using Swagger or DRF browsable API.

---

##  Key Components

* `store/`: Forms, models, views, static files, templates for customers.
* `vendor/`: Templates, models, and forms for vendors.
* `api/`: Views, serializers, and routing for REST API.
* `client/`: Scripts for testing image uploads and order simulation.


## 📄 License

This project is licensed under the **MIT License**. Feel free to use and modify.

---

##  Author

**Amit Giri**
Passionate about Linux, Python, and creating effective tech solutions.
Feel free to contribute or reach out for collaboration!

---

##  Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.
