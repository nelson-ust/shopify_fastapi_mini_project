# Shopify FastAPI Mini Project

## Project Description
This Shopify FastAPI Mini Project is designed to integrate with the Shopify API, leveraging FastAPI's capabilities to fetch and display order data based on customer IDs. FastAPI's asynchronous features and its compatibility with modern web services make it an ideal choice for this kind of integration.


![Swagger UI](swagger-ui.jpeg)
![Unit Test Outcome](unit_test.jpeg)

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Installation Guide

### Step 1: Clone the Repository

Clone the project repository from GitHub to your local machine:

```bash
git clone https://github.com/nelson-ust/shopify_fastapi_mini_project.git
cd shopify_fastapi_mini_project
```

### Step 2: Set Up a Virtual Environment
Creating a virtual environment is recommended to manage your Python dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

On Windows:

```bash
venv\Scripts\activate
```
On macOS and Linux:

```bash
source venv/bin/activate
```
### Step 3: Install Dependencies
Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Step 4: Environment Variables
Create a .env file in the root of your project and add the necessary environment variables:

```bash
SHOP_URL=yourshopifyshop.myshopify.com
ACCESS_TOKEN=youraccesstoken
```
Replace the values with your actual Shopify credentials.

### Step 5: Run the Application
Start the FastAPI server using Uvicorn:

```bash
uvicorn app.main:app --reload
```
### Step 6: Access the Application
Open a web browser and navigate to http://localhost:8000. You should see the FastAPI application running.

Access the API documentation at http://localhost:8000/docs to interact with the API.

### Step 7: Running Tests
To ensure the application works as expected, run the unit tests:

```bash
pytest
```
## Troubleshooting

If you encounter any issues, ensure you have the correct versions of Python and pip installed. Also, make sure all environment variables in the .env file are correctly set.
