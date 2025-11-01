# GeminiNanoBanana API Documentation

Welcome to the GeminiNanoBanana API! This document provides a clear and comprehensive guide to interacting with the available endpoints.

**Base URL**: `http://127.0.0.1:8000/` (for local development) or your production URL.

---

## Authentication

This section details the endpoints for user authentication.

### 1. User Signup

Create a new user account.

*   **Endpoint**: `/api/register`
*   **Method**: `POST`
*   **Description**: This endpoint allows new users to register. It requires a unique username, a valid email address, and a password.
*   **Headers**:
    *   `Content-Type`: `application/json`
*   **Request Body**:

    ```json
    {
        "username": "your_username",
        "email": "user@example.com",
        "password": "your_password"
    }
    ```

*   **Example `curl` Request**:

    ```bash
    curl -X POST \
      http://127.0.0.1:8000/api/register \
      -H 'Content-Type: application/json' \
      -d '{
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "a_strong_password"
    }'
    ```

*   **Success Response (201 Created)**:
    *   The user's `username` and `email` are returned upon successful registration.

    ```json
    {
        "username": "newuser",
        "email": "newuser@example.com"
    }
    ```

*   **Error Responses**:
    *   `400 Bad Request`: If the request body is missing required fields or if the data is invalid (e.g., email already exists).

### 2. User Login

Authenticate a user and create a session.

*   **Endpoint**: `/api/login`
*   **Method**: `POST`
*   **Description**: This endpoint allows users to log in with their email and password. A successful login will create a session and return a session cookie.
*   **Headers**:
    *   `Content-Type`: `application/json`
*   **Request Body**:

    ```json
    {
        "email": "user@example.com",
        "password": "your_password"
    }
    ```

*   **Example `curl` Request**:

    ```bash
    curl -X POST \
      http://127.0.0.1:8000/api/login \
      -H 'Content-Type: application/json' \
      -c cookie-jar.txt \ # Use -c to save the session cookie
      -d '{
        "email": "newuser@example.com",
        "password": "a_strong_password"
    }'
    ```

*   **Success Response (200 OK)**:
    *   A `sessionid` cookie is set in the response headers, which should be included in subsequent requests to authenticated endpoints.
    *   The response body will contain a message and the user's email.

    ```json
    {
        "message": "development in progress",
        "email": "user@example.com"
    }
    ```

### 3. User Logout

Log out the currently authenticated user.

*   **Endpoint**: `/api/logout`
*   **Method**: `POST`
*   **Description**: This endpoint logs out the user by clearing their session.

*   **Example `curl` Request**:

    ```bash
    curl -X POST \
      http://127.0.0.1:8000/api/logout \
      -b cookie-jar.txt # Use -b to send the session cookie
    ```

*   **Success Response (200 OK)**:
    *   An empty response is returned upon successful logout.

### 4. Get User Details

Retrieve the details of the currently authenticated user.

*   **Endpoint**: `/api/user`
*   **Method**: `GET`
*   **Authentication**: Session Authentication required.
*   **Description**: This endpoint returns the `email` and `username` of the currently logged-in user.

*   **Example `curl` Request**:

    ```bash
    curl -X GET \
      http://127.0.0.1:8000/api/user \
      -b cookie-jar.txt # Send the session cookie for authentication
    ```

*   **Success Response (200 OK)**:

    ```json
    {
        "user": {
            "email": "newuser@example.com",
            "username": "newuser"
        }
    }
    ```
