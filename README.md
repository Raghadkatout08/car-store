# car-store

## Overview

This project implements a Django application for managing car records, providing full CRUD (Create, Retrieve, Update, Delete) functionality.

## Features

- **Car Model**: Contains fields for model, brand, price, is_bought, buyer_id, and buy_time.
- **CRUD Views**: List, detail, create, update, and delete views for Car model.
- **Navigation**: Easy navigation between pages.

## Getting Started

### Prerequisites

- Python 3.x
- Django 4.x
- Virtual environment tool (optional but recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:Raghadkatout08/car-store.git
   cd car-store

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    
5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser

6. **Run the server:**
    ```bash
    python manage.py runserver

### Running Tests
To run the tests, execute:
    ```python manage.py test```

### Usage

- Navigate to the home page of the application to view the list of cars.
- Use the provided forms and buttons to create, update, and delete car records.