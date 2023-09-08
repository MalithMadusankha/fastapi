# FAST API SERVER

## What is FastAPI ?

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It is designed to make it easy to build web APIs quickly and efficiently, with features like automatic validation, documentation generation, and built-in asynchronous support.

## Here are some key features and concepts associated with FastAPI:

1. **Automatic Validation**: FastAPI uses Python type hints to automatically validate incoming requests and generate appropriate response models. This helps reduce common API-related bugs and ensures that the data you receive and send is of the expected type.

2. **Automatic Documentation**: FastAPI generates interactive documentation for your API based on your code's type hints and docstrings. You can access this documentation through a web browser, which makes it easy for developers to understand how to use your API.

3. **Asynchronous Support**: FastAPI fully supports asynchronous programming, allowing you to build highly concurrent and efficient APIs. You can use Python's `async` and `await` keywords to handle asynchronous operations like database queries or external API calls.

4. **Dependency Injection**: FastAPI provides a powerful dependency injection system that allows you to manage dependencies in a clean and organized way. You can use dependencies to manage authentication, database connections, and other common tasks.

5. **Request and Response Models**: You can define request and response models using Pydantic, a data validation and parsing library. FastAPI uses these models to automatically validate and parse incoming requests and generate well-structured responses.

6. **Middleware**: FastAPI supports middleware, which allows you to add custom logic to handle requests and responses at various stages of the request-response cycle. This is useful for tasks like authentication, logging, and error handling.

7. **Routing**: FastAPI provides a straightforward way to define API routes and endpoints using decorators. You can easily specify the HTTP methods (GET, POST, PUT, DELETE, etc.) that each route should handle.

8. **WebSocket Support**: FastAPI also includes support for WebSocket connections, making it suitable for building real-time applications and chat systems.

FastAPI has gained popularity due to its performance, simplicity, and developer-friendly features. It's often used in web development projects, microservices, and building RESTful APIs. To get started with FastAPI, you can install it using pip and explore the official documentation and tutorials to learn how to create APIs using this framework.

## Create evevirment

`python -m venv myenv`

## Activate evevirment

`source myenv/Scripts/activate`

## Ref fastapi doc

`https://fastapi.tiangolo.com/`

## Run app

`uvicorn main:app --reload`
