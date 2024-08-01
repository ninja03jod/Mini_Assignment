from typing import List
from fastapi import FastAPI, HTTPException

app = FastAPI()

def is_main_diagonal_uniform(matrix: List[List[int]]) -> bool:
    if not matrix or len(matrix) != len(matrix[0]):
        return False  # The matrix is not square
    
    n = len(matrix)
    
    if n == 0:
        return True  # An empty matrix is trivially uniform

    # Get the value of the main diagonal from the top-left corner
    diag_value = matrix[0][0]
    
    # Check if all elements on the main diagonal are the same
    for i in range(n):
        if matrix[i][i] != diag_value:
            return False
    
    return True

@app.post("/check_diagonal")
async def check_diagonal(matrix: List[List[int]]):
    if not matrix:
        raise HTTPException(status_code=400, detail="Matrix cannot be empty")
    
    result = is_main_diagonal_uniform(matrix)
    return {"result": result}

# To run the app: uvicorn main:app --reload
