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

*   **Validation Rules**:
    *   `username`: Must be alphanumeric (no special characters).
    *   `username`: Must be at least 5 characters long.
    *   `username`: Must start with a letter.
    *   `email`: Must be a unique email address.
    *   `email`: Must contain an `@` symbol and end with either `.com` or `.in`.

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
    *   `400 Bad Request`: If the request body is missing required fields or if the data is invalid (e.g., email already exists, email format is incorrect).

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

*   **Error Responses**:
    *   `400 Bad Request`:
        *   `{"detail": "No account is associated with this email address."}`
        *   `{"detail": "The password you entered is incorrect."}`

### 3. User Logout

Log out the currently authenticated user.

*   **Endpoint**: `/api/logout`
*   **Method**: `POST`
*   **Authentication**: Session Authentication required.
*   **Description**: This endpoint logs out the user by clearing their session.

*   **Example `curl` Request**:

    ```bash
    curl -X POST \
      http://127.0.0.1:8000/api/logout \
      -b cookie-jar.txt # Send the session cookie
    ```

*   **Success Response (200 OK)**:
    *   An empty response is returned upon successful logout.

*   **Error Responses**:
    *   `401 Unauthorized`: If the user is not authenticated.

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

### 5. Change Password

Change the password for the currently authenticated user.

*   **Endpoint**: `/api/change-password/`
*   **Method**: `POST`
*   **Authentication**: Session Authentication required.
*   **Description**: This endpoint allows a logged-in user to change their password by providing their old password and a new password (with confirmation).
*   **Headers**:
    *   `Content-Type`: `application/json`
*   **Request Body**:

    ```json
    {
        "old_password": "current_password",
        "new_password": "new_strong_password",
        "confirm_new_password": "new_strong_password"
    }
    ```

*   **Example `curl` Request**:

    ```bash
    curl -X POST \
      http://127.0.0.1:8000/api/change-password/ \
      -H 'Content-Type: application/json' \
      -b cookie-jar.txt \ # Send the session cookie for authentication
      -d '{
        "old_password": "a_strong_password",
        "new_password": "a_even_stronger_password",
        "confirm_new_password": "a_even_stronger_password"
    }'
    ```

*   **Success Response (200 OK)**:

    ```json
    {
        "detail": "Password updated successfully."
    }
    ```

*   **Error Responses**:
    *   `400 Bad Request`:
        *   `{"detail": "New passwords must match."}`
        *   `{"detail": "Old password is not correct."}`
    *   `401 Unauthorized`: If the user is not authenticated.

---

## Nano Banana Cards

### 1. Create a Card

Create a new Nano Banana Card.

*   **Endpoint**: `/api/cards/create/`
*   **Method**: `POST`
*   **Authentication**: Session Authentication required.
*   **Description**: This endpoint allows a logged-in user to create a new card by providing a prompt and an image.
*   **Headers**:
    *   `Content-Type`: `multipart/form-data`
*   **Request Body**:
    *   `prompt` (text)
    *   `image` (file)

*   **Example `curl` Request**:

    ```bash
    curl -X POST \
      http://127.0.0.1:8000/api/cards/create/ \
      -H "Content-Type: multipart/form-data" \
      -b cookie-jar.txt \ # Send the session cookie for authentication
      -F "prompt=A beautiful banana" \
      -F "image=@/path/to/your/image.jpg"
    ```

*   **Success Response (201 Created)**:

    ```json
    {
        "id": 1,
        "prompt": "A beautiful banana",
        "image": "/media/cards/image.jpg",
        "created_at": "2025-11-02T12:00:00Z"
    }
    ```

*   **Error Responses**:
    *   `400 Bad Request`: If the request body is missing required fields or if the data is invalid.
    *   `401 Unauthorized`: If the user is not authenticated.

### 2. User Dashboard

Retrieve all cards for the currently authenticated user.

*   **Endpoint**: `/api/dashboard/`
*   **Method**: `GET`
*   **Authentication**: Session Authentication required.
*   **Description**: This endpoint returns a list of all Nano Banana Cards created by the currently logged-in user.

*   **Example `curl` Request**:

    ```bash
    curl -X GET \
      http://127.0.0.1:8000/api/dashboard/ \
      -b cookie-jar.txt # Send the session cookie for authentication
    ```

*   **Success Response (200 OK)**:

    ```json
    [
        {
            "id": 1,
            "prompt": "A beautiful banana",
            "image": "/media/cards/image.jpg",
            "created_at": "2025-11-02T12:00:00Z"
        },
        {
            "id": 2,
            "prompt": "A funny banana",
            "image": "/media/cards/another_image.jpg",
            "created_at": "2025-11-02T12:05:00Z"
        }
    ]
    ```

*   **Error Responses**:
    *   `401 Unauthorized`: If the user is not authenticated.
