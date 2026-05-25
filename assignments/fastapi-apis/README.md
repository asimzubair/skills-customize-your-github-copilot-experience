# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a simple REST API using FastAPI to practice building endpoints, validating request data, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create the FastAPI app

#### Description

Set up a FastAPI application with a root route and a basic item retrieval endpoint.

#### Requirements
Completed project should:

- Define a FastAPI `app` instance
- Add a `GET /` route that returns a welcome JSON message
- Add a `GET /items/{item_id}` route that returns item details by ID
- Return a `404` error when the requested item is not found

### 🛠️ Add item creation and validation

#### Description

Create a Pydantic model for items and implement an endpoint that accepts JSON data to create a new item.

#### Requirements
Completed project should:

- Define an `Item` model using `pydantic.BaseModel`
- Add a `POST /items` route that accepts an item body
- Validate the incoming item data automatically using FastAPI
- Store the new item in an in-memory list and return it in the response

### 🛠️ Update and delete items

#### Description

Implement update and delete endpoints so clients can modify or remove items from the API.

#### Requirements
Completed project should:

- Add a `PUT /items/{item_id}` route that updates the item fields
- Add a `DELETE /items/{item_id}` route that removes the item
- Return a `404` error when updating or deleting a missing item
- Return the updated item after a successful update
