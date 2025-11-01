# GeminiNanoBanana API Documentation

This document provides details on the API endpoints for the GeminiNanoBanana project.

**Base URL**: `http://127.0.0.1:8000/` (for local development) or your production URL.

---

## Authentication

### 1. User Signup

Create a new user account.

*   **URL**: `/api/register`
*   **Method**: `POST`
*   **Headers**:
    *   `Content-Type`: `application/json`
*   **Body**:

    ```json
    {
        "username": "testuser",
        "email": "test@example.com",
        "password": "yourpassword"
    }
    ```

*   **Example Request**:

    ```bash
    curl -X POST \
      http://127.0.0.1:8000/api/register \
      -H 'Content-Type: application/json' \
      -d '{
        "username": "testuser",
        "email": "test@example.com",
        "password": "yourpassword"
    }'
    ```

*   **Success Response (201 Created)**:

    ```json
    {
        "username": "testuser",
        "email": "test@example.com"
    }
    ```

### 2. User Login

Authenticate a user and start a session.

*   **URL**: `/api/login`
*   **Method**: `POST`
*   **Headers**:
    *   `Content-Type`: `application/json`
*   **Body**:

    ```json
    {
        "email": "test@example.com",
        "password": "yourpassword"
    }
    ```

*   **Example Request**:

    ```bash
    curl -X POST \
      http://127.0.0.1:8000/api/login \
      -H 'Content-Type: application/json' \
      -c cookie-jar.txt \ # Store session cookie
      -d '{
        "email": "test@example.com",
        "password": "yourpassword"
    }'
    ```

*   **Success Response (200 OK)**:
    *   The response body will contain the user data.
    *   A `sessionid` cookie will be set in the response headers.

### 3. User Logout

Log out the currently authenticated user and end the session.

*   **URL**: `/api/logout`
*   **Method**: `POST`

*   **Example Request**:

    ```bash
    curl -X POST \
      http://127.0.0.1:8000/api/logout \
      -b cookie-jar.txt # Send session cookie
    ```

*   **Success Response (200 OK)**:
    *   An empty response.

### 4. Get User Details

Retrieve the details of the currently authenticated user.

*   **URL**: `/api/user`
*   **Method**: `GET`
*   **Authentication Required**: Yes (Session Authentication)

*   **Example Request**:

    ```bash
    curl -X GET \
      http://127.0.0.1:8000/api/user \
      -b cookie-jar.txt # Send session cookie
    ```

*   **Success Response (200 OK)**:

    ```json
    {
        "user": {
            "email": "test@example.com",
            "username": "testuser"
        }
    }
    ```
