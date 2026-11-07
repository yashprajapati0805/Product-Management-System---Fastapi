# Product Management System – REST API

A RESTful Product Management System built using **Python, FastAPI, SQLAlchemy, and PostgreSQL**. The application provides API endpoints to perform CRUD (Create, Read, Update, Delete) operations on product records.

## Features

- Create new products
- Retrieve all products
- Retrieve products by ID
- Update existing product details
- Delete products
- PostgreSQL database integration
- SQLAlchemy ORM for database operations
- Pydantic models for request validation
- Interactive API documentation with Swagger UI

## Tech Stack

| Technology | Purpose                         |
|------------|---------------------------------|
| Python     | Programming language            |
| FastAPI    | Backend framework               |
| PostgreSQL | Relational database             |
| SQLAlchemy | Object Relational Mapping (ORM) |
| Pydantic   | Data validation                 |
| pg8000     | PostgreSQL database driver      |
| Uvicorn    | ASGI server                     |
| REST API   | Application architecture        |

## API Endpoints

| Method | Endpoint | Description |
|--------|---------------------|-------------------|
| GET    | `/`                 | Welcome message   |
| GET    | `/products`         | Get all products  |
| GET    | `/products/{id}`    | Get product by ID |
| POST   | `/products`         | Add a new product |
| PUT    | `/products?id={id}` | Update a product  |
| DELETE | `/products?id={id}` | Delete a product  |

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/product-management-system-fastapi.git
cd product-management-system-fastapi
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

Create a PostgreSQL database and configure your `.env` file in the project root:

```env
DATABASE_URL=postgresql+pg8000://username:password@localhost:5432/product_management
```

Replace the username, password, and database name with your PostgreSQL credentials.

### 5. Run the application

```bash
uvicorn main:app --reload
```

## API Documentation

After starting the application, access:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Project Status

Under Development.

## Author

**Yash Prajapati**

GitHub: https://github.com/yashprajapati0805