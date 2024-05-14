# Bitpin

## Project Overview

Bitpin Technical Task

## Getting Started

### Installation

1. Clone this repository to your local machine

2. Create and activate a virtual environment based on your OS:

```shell
python3 -m venv .venv
source .venv/bin/activate
```

3. Install project dependencies:

```shell
pip install -r requirements.txt
```

4. Apply database migration commands:

```shell
python manage.py makemigrations
python manage.py migrate
```

## Endpoints

### BlogApp

#### Get Posts

- **URL:** `/api/posts`
- **Method:** `GET`
- **Purpose:** Get list of posts.
- **Response:**
  ```json
    [
    ...,
    {
        "id": 2,
        "average_rating": 2.5,
        "rating_count": 2,
        "title": "test title",
        "content": "test content",
        "created_at": "2024-05-13T14:50:33.362683Z"
    },
    ...
  ]
  ```
#### Post Rating

- **URL:** `/api/posts/<int:post_id>/`
- **Method:** `POST`
- **Purpose:** Post a rating to a post.
- **Parameters:**
  - `rating`: integer value between 0 and 5.
- **Responses:**
  - `200 OK`
  - `400 Bad Request`
  - `302 Redirect`: If user is not logged in

## Solution
To solve the problem of too many requests, I used login_required decorator to force the user to login for rating a post and also set throttle to limit the number of requests per minute.
