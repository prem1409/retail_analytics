# Retail Analytics Platform

A REST API built with FastAPI, SQLAlchemy, and MySQL for managing retail products, sales transactions, inventory tracking, and business analytics.

## Overview

This application provides:

* Product Management
* Sales Recording
* Inventory Tracking
* Revenue Analytics
* Top Product Analytics
* Category Revenue Analytics
* Low Stock Monitoring

The project demonstrates:

* REST API Development
* FastAPI Framework
* SQLAlchemy ORM
* MySQL Integration
* Service Layer Architecture
* Repository Pattern
* Analytics Query Development

---

# Technology Stack

| Technology  | Purpose              |
| ----------- | -------------------- |
| Python 3.9+ | Programming Language |
| FastAPI     | REST API Framework   |
| SQLAlchemy  | ORM                  |
| MySQL       | Database             |
| Pydantic    | Request Validation   |
| Uvicorn     | ASGI Server          |

---

# Project Structure

```text
retail-analytics/

├── app/
│   ├── database.py
│   ├── main.py
│   │
│   ├── models/
│   │   ├── product.py
│   │   ├── sale.py
│   │   └── store.py
│   │
│   ├── schemas/
│   │   └── product.py
│   │
│   ├── repositories/
│   │   └── product_repository.py
│   │
│   ├── services/
│   │   ├── analytics_service.py
│   │   └── inventory_service.py
│   │
│   └── routers/
│       ├── analytics.py
│       ├── products.py
│       └── sales.py
│
├── create_tables.py
├── requirements.txt
└── README.md
```

---

# Features

## Product Management

Manage retail products.

### Supported Operations

* Create Product
* Get All Products
* Get Product By ID
* Delete Product

---

## Sales Management

Track sales transactions.

### Supported Operations

* Record Sale
* View All Sales

When a sale is recorded:

* Inventory is automatically reduced
* Sales records are stored
* Analytics are updated

---

## Analytics

### Revenue Analytics

Calculate total revenue generated from sales.

### Top Products

Identify products with the highest sales volume.

### Category Revenue

Calculate revenue by product category.

### Low Stock Report

Identify products with inventory below threshold levels.

---

# Database Schema

## Products Table

```sql
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    category VARCHAR(100),
    price DECIMAL(10,2),
    stock_quantity INT
);
```

---

## Stores Table

```sql
CREATE TABLE stores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    city VARCHAR(255)
);
```

---

## Sales Table

```sql
CREATE TABLE sales (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    store_id INT,
    quantity INT,
    sale_date DATETIME,
    FOREIGN KEY (product_id)
        REFERENCES products(id),

    FOREIGN KEY (store_id)
        REFERENCES stores(id)
);
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/retail-analytics.git

cd retail-analytics
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

Example requirements:

```txt
fastapi
uvicorn
sqlalchemy
pymysql
pydantic
python-multipart
```

---

# MySQL Configuration

Create database:

```sql
CREATE DATABASE retail_analytics;
```

Update connection string in `database.py`:

```python
DATABASE_URL = (
    "mysql+pymysql://root:password@localhost:3306/retail_analytics"
)
```

---

# Create Database Tables

```bash
python create_tables.py
```

Expected output:

```text
tables created
```

---

# Running the Application

Start the API server:

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

ReDoc Documentation:

```text
http://localhost:8000/redoc
```

---

# API Endpoints

## Health Check

### GET /

Returns application status.

#### Response

```json
{
  "status": "running"
}
```

---

# Products

## Get All Products

### GET /products/

#### Response

```json
[
  {
    "id": 1,
    "name": "Power Drill",
    "category": "Tools",
    "price": 99.99,
    "stock_quantity": 50
  }
]
```

---

## Create Product

### POST /products/

#### Request

```json
{
  "name": "Power Drill",
  "category": "Tools",
  "price": 99.99,
  "stock_quantity": 50
}
```

#### Response

```json
{
  "id": 1,
  "name": "Power Drill",
  "category": "Tools",
  "price": 99.99,
  "stock_quantity": 50
}
```

---

## Get Product By ID

### GET /products/{product_id}

#### Example

```http
GET /products/1
```

---

## Delete Product

### DELETE /products/{product_id}

#### Example

```http
DELETE /products/1
```

#### Response

```json
{
  "message": "deleted"
}
```

---

# Sales

## Record Sale

### POST /sales/

#### Parameters

| Parameter  | Type | Required |
| ---------- | ---- | -------- |
| product_id | int  | Yes      |
| store_id   | int  | Yes      |
| quantity   | int  | Yes      |

#### Example

```http
POST /sales/?product_id=1&store_id=1&quantity=5
```

#### Response

```json
{
  "message": "sale recorded"
}
```

---

## Get All Sales

### GET /sales/

#### Response

```json
[
  {
    "id": 1,
    "product_id": 1,
    "store_id": 1,
    "quantity": 5
  }
]
```

---

# Analytics

## Total Revenue

### GET /analytics/revenue

#### Response

```json
{
  "revenue": 24500.75
}
```

---

## Top Products

### GET /analytics/top-products

#### Response

```json
[
  {
    "product_name": "Power Drill",
    "units_sold": 125
  }
]
```

---

## Category Revenue

### GET /analytics/category-revenue

#### Response

```json
[
  {
    "category": "Tools",
    "revenue": 10500.50
  }
]
```

---

## Low Stock Products

### GET /analytics/low-stock

Returns products with inventory lower than 10 units.

#### Response

```json
[
  {
    "id": 5,
    "name": "Hammer",
    "stock_quantity": 4
  }
]
```

---

# Analytics Queries

## Top Selling Products

```sql
SELECT
    p.name,
    SUM(s.quantity) AS units_sold
FROM sales s
JOIN products p
ON p.id = s.product_id
GROUP BY p.name
ORDER BY units_sold DESC;
```

---

## Revenue Calculation

```sql
SELECT
    SUM(p.price * s.quantity)
FROM sales s
JOIN products p
ON p.id = s.product_id;
```

---

## Low Stock Products

```sql
SELECT *
FROM products
WHERE stock_quantity < 10;
```

---

# Future Enhancements

* JWT Authentication
* Role-Based Access Control
* Product Search Filters
* Pagination
* Store Analytics
* Forecasting
* CSV Import
* Audit Logging
* Redis Caching
* Unit Testing
* Integration Testing
* Docker Deployment

---

# Author

Retail Analytics Platform

Built with FastAPI, SQLAlchemy, and MySQL.
