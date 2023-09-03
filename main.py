from fastapi import FastAPI
from routers.wellknown import wellknown
from fastapi.middleware.cors import CORSMiddleware
import json
app = FastAPI()
app.include_router(wellknown)
app.add_middleware(CORSMiddleware, allow_origins=["https://chat.openai.com"])
with open("./data/products.json", "r") as f:
    products = json.load(f)

with open("./data/employees.json", "r") as e:
    employees = json.load(f)

@app.get("/products", summary="Get a list of products", operation_id="getProducts")
async def get_products(query: str = None):
    """
    Returns a list of products, optionally filtered by providing a query parameter.
    """
    if query:
        keywords = query.lower().split()
        return [
            product
            for product in products
            if all(keyword in str(product.values()).lower() for keyword in keywords)
        ]
    return products

@app.get("/employees", summary="Get a list of employees", operation_id="getEmployees")
async def get_employees(query: str = None):
    
    # Returns a list of employees, optionally filtered by providing a query parameter.
    if query:
        keywords = query.lower().split()
        return [
            employee
            for employee in employees
            if all(keyword in str(employee.values()).lower() for keyword in keywords)
        ]
    """ employees = [{
      "name": "Eli",
      "description": "Most valuable employee",
      "category": "CSA",
      "size": "42",
      "price": 149.99
    },
    {
      "name": "Marina",
      "description": "Less valuable employee",
      "category": "Free-lancer",
      "size": "36",
      "price": 129.99
    }] """
    return employees