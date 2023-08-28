from fastapi import FastAPI, HTTPException, Body
import re
import json

app = FastAPI()

def reformat_string(input_string):
    questions_and_answers = re.findall(r"QS: (.+?) Answer: (.+?)(?=(?:\s*QS:|$))", input_string)
    reformatted_list = []
    
    for question, answer in questions_and_answers:
        prompt = {"prompt": question.strip()}
        completion = {"completion": answer.strip()}
        reformatted_list.append(json.dumps({**prompt, **completion}))
    
    return reformatted_list

@app.post("/reformat")
async def reformat_input_string(input_data: dict = Body(...)):
    try:
        input_string = input_data["input_string"]
        reformatted_output = reformat_string(input_string)
        return reformatted_output
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

