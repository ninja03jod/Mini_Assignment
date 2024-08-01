from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import string

app = FastAPI()

class Sentence(BaseModel):
    text: str

def is_pangram(sentence: str) -> bool:
    # Convert the sentence to lowercase to handle case insensitivity
    sentence = sentence.lower()
    
    # Create a set of all lowercase alphabet letters
    alphabet_set = set(string.ascii_lowercase)
    
    # Create a set of characters present in the sentence
    sentence_set = set(sentence)
    
    # Check if all alphabet letters are in the sentence
    return alphabet_set.issubset(sentence_set)

@app.post("/check_pangram")
def check_pangram(sentence: Sentence):
    if not sentence.text:
        raise HTTPException(status_code=400, detail="Empty sentence provided")
    
    result = is_pangram(sentence.text)
    return {"is_pangram": result}
