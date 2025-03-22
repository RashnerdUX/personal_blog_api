# Flask Blogging API

## Overview
This is a simple RESTful API for a blogging platform built with Flask and Flask-RESTful. It allows users to create, read, update, and delete blog posts while storing the data in an SQLite database.

## Features
- Create a new blog post
- Retrieve all blog posts
- Retrieve a single blog post by ID
- Update a blog post
- Delete a blog post
- Store and retrieve tags as lists

## Technologies Used
- Python
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- SQLite

## Installation

### Prerequisites
Make sure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/).

### Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/blogging-api.git
   cd blogging-api
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python main.py
   ```

## API Endpoints

### 1. Create a Blog Post
- **Endpoint:** `POST /`
- **Request Body (JSON):**
  ```json
  {
      "title": "Why Women Kill",
      "category": "Movies",
      "body": "This is a movie set across three timelines in the same house",
      "tags": ["movie", "show", "netflix", "amazon prime"]
  }
  ```
- **Response:**
  ```json
  {
      "message": "Blog post created successfully!"
  }
  ```

### 2. Get All Blog Posts
- **Endpoint:** `GET /`
- **Response:**
  ```json
  [
      {
          "id": 1,
          "date": "2025-03-18T12:00:00",
          "title": "Why Women Kill",
          "category": "Movies",
          "body": "This is a movie set across three timelines in the same house",
          "tags": ["movie", "show", "netflix", "amazon prime"]
      }
  ]
  ```

### 3. Get a Specific Blog Post
- **Endpoint:** `GET /blogpost/<blog_id>`
- **Response:**
  ```json
  {
      "id": 1,
      "date": "2025-03-18T12:00:00",
      "title": "Why Women Kill",
      "category": "Movies",
      "body": "This is a movie set across three timelines in the same house",
      "tags": ["movie", "show", "netflix", "amazon prime"]
  }
  ```

### 4. Update a Blog Post
- **Endpoint:** `PUT /blogpost/<blog_id>`
- **Request Body (JSON):**
  ```json
  {
      "title": "Why Women Kill - Updated",
      "category": "TV Series",
      "body": "A gripping show with multiple timelines",
      "tags": ["drama", "thriller"]
  }
  ```
- **Response:**
  ```json
  {
      "message": "Blog post modified successfully!"
  }
  ```

### 5. Delete a Blog Post
- **Endpoint:** `DELETE /blogpost/<blog_id>`
- **Response:**
  ```json
  {
      "message": "Blog post deleted successfully!"
  }
  ```

## Database Schema
The database consists of a single table called `blog_model`, with the following columns:
- `id` (Integer, Primary Key)
- `date` (DateTime, defaults to current time)
- `title` (String, nullable)
- `category` (String, nullable)
- `body` (String, nullable)
- `tags` (Text, stored as a JSON string but accessed as a list)

## Running in Debug Mode
To enable Flask debug mode for development, run:
```sh
python main.py
```
The app will automatically reload when you make changes to the code.

## Contributing
Feel free to fork this repository and submit pull requests for improvements.

## License
This project is open-source and available under the MIT License.

## Link to Project
Here's the link to the roadmap.sh project that inspired the project
Link - https://roadmap.sh/projects/blogging-platform-api
