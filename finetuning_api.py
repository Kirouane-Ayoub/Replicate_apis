from fastapi import FastAPI, File, UploadFile, Form
import replicate
import os

app = FastAPI()

@app.post("/train")
async def train(
    destination: str = Form(...),
    train_batch_size: int = Form(...),
    gradient_accumulation_steps: int = Form(...),
    num_train_epochs: int = Form(...),
    warmup_ratio: float = Form(...),
    train_data: UploadFile = File(...)
):
    try:
        os.environ["REPLICATE_API_TOKEN"] = "api_key"
        version = "a16z-infra/llama-2-7b-chat:4f0b260b6a13eb53a6b1891f089d57c08f41003ae79458be5011303d81a394dc"

        training = replicate.trainings.create(
            version=version,
            input={
                "train_data": train_data.file,
                "train_batch_size": train_batch_size,
                "gradient_accumulation_steps": gradient_accumulation_steps,
                "num_train_epochs": num_train_epochs,
                "warmup_ratio": warmup_ratio
            },
            destination=destination
        )

        return {"training": training}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
