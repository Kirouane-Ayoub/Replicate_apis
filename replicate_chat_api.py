from fastapi import FastAPI, Form
from langchain.chains import ConversationChain
from langchain.llms import Replicate
os.environ["REPLICATE_API_TOKEN"] = "api_key"
app = FastAPI()

@app.post("/chat")
async def chat(
    model: str = Form(...),
    conversationid: str = Form(...),
    index_name: str = Form(...),
    environment: str = Form(...),
    api_key: str = Form(...),
    knowledge: list = Form(...),
    text_input: str = Form(...)
):
    try:
        llm = Replicate(
            model=model,
            input={"temperature": 1, "max_length": 2048, "top_p": 1},
        )
        chat = ConversationChain(
            llm=llm,
            verbose=False)
        chat.prompt.template = \
            """
            ###User:

            Personal details :
            {history}



            Current conversation:
            ###User: {input}
            ###Assistant:"""
        response = chat.predict(input=text_input)
        return {"response": response}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
