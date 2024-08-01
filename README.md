# FastAPI Matrix and Sentence Checkers

This FastAPI application provides two endpoints:
1. **Check if all elements along the main diagonal of a matrix are the same**.
2. **Check if a given sentence is a pangram** (contains every letter of the English alphabet at least once).

## Prerequisites

- Python 3.12.4

## Installation

Follow these steps to set up and run the FastAPI application:

1. **Clone the Repository**

   Open your terminal or command prompt and clone the repository with:

   ```bash
   git clone https://github.com/ninja03jod/Mini_Assignment.git
   cd Mini_Assignment

# Running the Application

### 1.Run the FastAPI Server

Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn diagonal_check:app --reload

This command will start the server and make it available at http://127.0.0.1:8000. The --reload flag ensures the server automatically reloads when you make changes to the code.

### 2.Access the API Documentation

Open your web browser and navigate to:

http://127.0.0.1:8000/docs

The FastAPI documentation provides an interactive interface to test the endpoints.

Inside this you have to Try it out with 

### API Endpoints
`/check_diagonal`
#### Method: POST

#### Description: Checks if all elements along the main diagonal of the given matrix are the same.

#### Request Body:

Content-Type: application/json

Example JSON payload:
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

#### Response:

Status Code: 200 OK

Content-Type: application/json

Example response:
{
  "is_diagonal_same": true
}

`/check_pangram`

#### Method: POST

#### Description: Checks if a given sentence is a pangram (a sentence containing every letter of the English alphabet at least once).

#### Request Body:

Content-Type: application/json

Example JSON payload:
{
  "text": "The quick brown fox jumps over the lazy dog."
}

#### Response:

Status Code: 200 OK

Content-Type: application/json

Example response:
{
  "is_pangram": true
}

## SQL Query Example

### Explanation:

1. Join the Tables: Joins the employees table with the departments table based on department_id.
2. Select Columns: Selects the department name and calculates the average salary.
3. Group By: Groups the results by department name to compute the average salary for each department.


This `README.md` file provides all necessary details for setting up and running the FastAPI application, as well as testing the API endpoints and SQL query example. Adjust `<your-repository-url>` and `<your-repository-directory>` with your actual repository details.
