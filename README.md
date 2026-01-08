
## Notes API – Backend Assignment

## Introduction

This project is a simple backend application developed as part of a technical assessment.
The goal of this project is to build a REST API using **FastAPI** that allows users to create, view, update, and delete notes.

While building this project, I focused on understanding core backend concepts like API design, database interaction, validation, and testing.

## Technologies Used

* Python 3.13.2
* FastAPI
* SQLAlchemy
* SQLite 
* Pydantic
* Uvicorn
* Pytest

## Project Structure

Project_Notes/
│
├── app/
│   ├── main.py        # FastAPI app and API routes
│   ├── database.py    # Database connection setup
│   ├── models.py      # Database table models
│   ├── schemas.py     # Request and response schemas
│   └── crud.py        # Database operations
│
├── tests/
│   ├── conftest.py    # Pytest configuration
│   └── test_notes.py  # API test cases
│
├── .env.example
├── requirements.txt
└── README.md


## How to Set Up the Project

### 1.Clone the Repository
 I have used Command prompt
git clone <repository-url>
cd Project_Notes


### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3. Install Required Packages

pip install -r requirements.txt

## Run the Application

python -m uvicorn app.main:app --reload

Once the server is running, open your browser and go to:

* API Base URL:
  `http://127.0.0.1:8000`

* Swagger API Documentation:
  `http://127.0.0.1:8000/docs`

## API - Endpoints

### ➕ Create a Note

**POST** `/notes`

Example request:

json :
{
  "title": "My first note",
  "content": "I am learning FastAPI step by step"
}

### Get a Note by ID

**GET** `/notes/{note_id}`


### Update a Note

**PUT** `/notes/{note_id}`

Example request:

json :
{
  "title": "Updated note",
  "content": "This note was updated"
}

### Delete a Note

**DELETE** `/notes/{note_id}`

Returns:

* `204 No Content` if deletion is successful


## External API Usage

An external sentiment analysis API is used to analyze the content of each note.

* The sentiment result is stored along with the note
* If the external API fails, a default value is used
* This helps keep the application stable even if the API is unavailable


## Testing

Basic tests are written using **pytest**.

To run tests:  * i uesd to run in cmd
pytest

The tests check:

* Note creation
* Note retrieval
* API response status codes

##  Error Handling

* `404 Not Found` → Note ID does not exist
* `422 Validation Error` → Invalid request data
* `500 Internal Server Error` → Handled safely inside the application

## Environment Variables

A `.env.example` file is provided as a reference.

Sensitive information should not be committed to the repository.

## Author

**Arthidevi R**

## Project Status

* All required APIs implemented
* Tested using Swagger and pytest
* Meets assessment requirements
